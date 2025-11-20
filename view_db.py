import sqlite3
import os

db_path = 'backend/example.db'

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print("=" * 60)
    print(f"DATABASE: {db_path}")
    print("=" * 60)
    print(f"\nTables found: {[t[0] for t in tables]}\n")
    
    # Show data from each table
    for table in tables:
        table_name = table[0]
        print(f"\n{'=' * 60}")
        print(f"TABLE: {table_name}")
        print("=" * 60)
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        print(f"Columns: {', '.join(column_names)}")
        
        # Get all rows
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        print(f"\nTotal rows: {len(rows)}\n")
        
        if rows:
            # Print header
            print(" | ".join(column_names))
            print("-" * 60)
            
            # Print rows
            for row in rows:
                print(" | ".join(str(cell) for cell in row))
        else:
            print("(No data)")
    
    conn.close()
    print("\n" + "=" * 60)
else:
    print(f"Database file not found at: {db_path}")
