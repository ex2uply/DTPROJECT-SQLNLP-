import sqlite3
import pandas as pd
import os
from typing import List, Dict, Any

class DBManager:
    def __init__(self, db_path: str = "example.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Load local Sales Data.csv into database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if database is already populated
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        existing_tables = cursor.fetchall()
        
        if not existing_tables:
            print("Loading Sales Data.csv...")
            try:
                # Load the CSV file from project root
                csv_path = os.path.join(os.path.dirname(__file__), '..', 'Sales Data.csv')
                
                if os.path.exists(csv_path):
                    df = pd.read_csv(csv_path)
                    
                    # Clean column names (replace spaces with underscores, lowercase)
                    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
                    
                    # Remove unnamed index column if it exists
                    if 'unnamed:_0' in df.columns:
                        df = df.drop('unnamed:_0', axis=1)
                    
                    # Save to SQLite
                    table_name = 'sales'
                    df.to_sql(table_name, conn, if_exists='replace', index=False)
                    print(f"[SUCCESS] Created table '{table_name}' with {len(df)} records")
                    print(f"[INFO] Columns: {', '.join(df.columns.tolist())}")
                    
                else:
                    print(f"[ERROR] Sales Data.csv not found at {csv_path}")
                    print("Creating sample data instead...")
                    self._create_sample_data(cursor, conn)
                    
                conn.commit()
                    
            except Exception as e:
                print(f"[ERROR] Error loading CSV: {e}")
                print("Creating sample data instead...")
                self._create_sample_data(cursor, conn)
        
        conn.close()

    def _create_sample_data(self, cursor, conn):
        """Fallback: Create sample data if CSV loading fails."""
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                order_id TEXT,
                product TEXT,
                quantity_ordered INTEGER,
                price_each REAL,
                order_date TEXT,
                purchase_address TEXT
            )
        ''')
        
        cursor.execute('SELECT count(*) FROM sales')
        if cursor.fetchone()[0] == 0:
            data = [
                ('1', 'Laptop', 1, 1200.00, '2023-01-15 10:00:00', '123 Main St, Boston, MA 02215'),
                ('2', 'Mouse', 2, 25.00, '2023-01-16 11:00:00', '456 Oak St, Seattle, WA 98101'),
                ('3', 'Keyboard', 1, 45.00, '2023-01-17 12:00:00', '789 Pine St, Austin, TX 73301'),
            ]
            cursor.executemany(
                'INSERT INTO sales (order_id, product, quantity_ordered, price_each, order_date, purchase_address) VALUES (?, ?, ?, ?, ?, ?)', 
                data
            )
            conn.commit()

    def execute_query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute a SQL query and return results as a list of dicts."""
        try:
            conn = sqlite3.connect(self.db_path)
            df = pd.read_sql_query(sql, conn)
            conn.close()
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"SQL Error: {e}")
            return [{"error": str(e)}]

    def get_schema(self) -> Dict[str, Any]:
        """Return the database schema with table and column information."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        schema = {}
        for table in tables:
            table_name = table[0]
            # Get column info for each table
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            schema[table_name] = [{"name": col[1], "type": col[2]} for col in columns]
        
        conn.close()
        return schema
    
    def get_sample_data(self, table_name: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Get sample data from a table for context."""
        try:
            sql = f"SELECT * FROM {table_name} LIMIT {limit}"
            return self.execute_query(sql)
        except:
            return []

    def get_unique_values(self, table_name: str, column_name: str, limit: int = 50) -> List[str]:
        """Get unique values for a column to help LLM understand context."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT DISTINCT {column_name} FROM {table_name} WHERE {column_name} IS NOT NULL LIMIT {limit}")
            values = [str(row[0]) for row in cursor.fetchall()]
            conn.close()
            return values
        except Exception as e:
            print(f"Error fetching unique values for {column_name}: {e}")
            return []
