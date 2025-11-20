import sqlite3
import pandas as pd
from typing import List, Dict, Any

class DBManager:
    def __init__(self, db_path: str = "example.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize a sample database for testing."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create a sample table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                quantity INTEGER,
                price REAL,
                date DATE
            )
        ''')
        
        # Check if empty and populate
        cursor.execute('SELECT count(*) FROM sales')
        if cursor.fetchone()[0] == 0:
            data = [
                ('Laptop', 5, 1200.00, '2023-01-15'),
                ('Mouse', 50, 25.00, '2023-01-16'),
                ('Keyboard', 30, 45.00, '2023-01-17'),
                ('Monitor', 10, 300.00, '2023-01-18'),
                ('Laptop', 3, 1200.00, '2023-02-01'),
            ]
            cursor.executemany('INSERT INTO sales (product_name, quantity, price, date) VALUES (?, ?, ?, ?)', data)
            conn.commit()
            
        conn.close()

    def execute_query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute a SQL query and return results as a list of dicts."""
        try:
            conn = sqlite3.connect(self.db_path)
            df = pd.read_sql_query(sql, conn)
            conn.close()
            return df.to_dict(orient='records')
        except Exception as e:
            return [{"error": str(e)}]

    def get_schema(self) -> str:
        """Return the database schema as a string for the LLM."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        return "\n".join([t[0] for t in tables if t[0]])
