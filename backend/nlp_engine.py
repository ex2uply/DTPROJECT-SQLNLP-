from typing import Dict, Any
import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

class NLPEngine:
    def __init__(self):
        # Load environment variables from .env file in backend directory
        env_path = Path(__file__).parent / '.env'
        load_dotenv(dotenv_path=env_path)
        
        # Configure Gemini API
        api_key = os.getenv('GEMINI_API_KEY', '')
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
            self.llm_enabled = True
            print("[SUCCESS] Gemini LLM initialized")
        else:
            self.llm_enabled = False
            print("[WARNING] GEMINI_API_KEY not set - LLM features disabled")
            print("   Set environment variable: GEMINI_API_KEY=your_key_here")

    def generate_sql(self, query: str, schema: Dict[str, Any]) -> tuple[str, str | None]:
        """
        Generate SQL from natural language query using Gemini LLM.
        Returns: (sql_query, warning_message)
        """
        if not self.llm_enabled:
            sql = self._fallback_sql_generation(query, schema)
            return sql, "⚠️ Gemini API key not configured. Using basic pattern matching."
        
        try:
            # Prepare schema information with explicit values for context
            schema_text = self._format_schema_with_context(schema)
            
            # Create prompt for Gemini
            prompt = f'''You are a SQLite expert. Convert the natural language query into a valid SQL query.

DATABASE SCHEMA & VALUES:
{schema_text}

RULES:
1. Use ONLY the provided table and column names.
2. For text filtering, use LIKE with % for partial matches (e.g. WHERE city LIKE '%San Francisco%').
3. For date filtering, the 'order_date' format is 'MM/DD/YY HH:MM'. Use strftime if needed.
4. Return ONLY the raw SQL query. No markdown, no explanations.
6. If the user asks for "count", they mean COUNT(*).

USER QUERY: {query}

SQL QUERY:'''
            
            # Generate SQL using Gemini with timeout
            print(f"Sending query to Gemini: {query}")
            response = self.model.generate_content(
                prompt,
                request_options={'timeout': 30}
            )
            sql = response.text.strip()
            
            # Clean up the response
            sql = sql.replace('```sql', '').replace('```', '').strip()
            sql = sql.replace(';', '').strip()
            
            print(f"Generated SQL: {sql}")
            return sql, None
            
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            print(f"[ERROR] LLM GENERATION FAILED: {error_type}: {error_msg}")
            import traceback
            traceback.print_exc()
            print("Falling back to pattern matching...")
            
            sql = self._fallback_sql_generation(query, schema)
            
            # Create user-friendly warning message based on error type
            if "ResourceExhausted" in error_type or "429" in error_msg:
                warning = "⚠️ Gemini API quota exceeded. Using basic pattern matching. Results may not match your exact query."
            elif "connection" in error_msg.lower() or "timeout" in error_msg.lower():
                warning = "⚠️ Cannot connect to Gemini API. Using basic pattern matching. Please check your internet connection."
            elif "invalid" in error_msg.lower() and "api" in error_msg.lower():
                warning = "⚠️ Invalid Gemini API key. Using basic pattern matching. Please check your configuration."
            else:
                warning = f"⚠️ Gemini API error: {error_type}. Using basic pattern matching."
            
            return sql, warning
    
    def _format_schema_with_context(self, schema: Dict[str, Any]) -> str:
        """Format schema information with sample values for better LLM context."""
        # We need to access DBManager to get values. 
        # Since NLPEngine is initialized separately, we'll do a quick connection here or pass it in.
        # For simplicity, we'll re-instantiate DBManager just to get values, or better, 
        # we should have passed DBManager to NLPEngine. 
        # But to avoid breaking changes, let's use a local instance.
        from db_manager import DBManager
        db = DBManager()
        
        schema_lines = []
        for table_name, columns in schema.items():
            schema_lines.append(f"Table: {table_name}")
            for col in columns:
                col_name = col['name']
                col_type = col['type']
                
                # Add sample values for key text columns
                extra_info = ""
                if col_name in ['city', 'product', 'purchase_address']:
                    values = db.get_unique_values(table_name, col_name, limit=20)
                    if values:
                        extra_info = f" -- Examples: {', '.join(values[:5])}..."
                
                schema_lines.append(f"  - {col_name} ({col_type}){extra_info}")
            schema_lines.append("")
            
        return "\n".join(schema_lines)
    
    def _fallback_sql_generation(self, query: str, schema: Dict[str, Any]) -> str:
        """Fallback SQL generation when LLM is not available."""
        # Get first table
        if not schema:
            return "SELECT 'No tables available' as error"
        
        table_name = list(schema.keys())[0]
        query_lower = query.lower()
        
        # Very basic pattern matching as fallback
        if 'count' in query_lower and 'by' in query_lower:
            # Try to find a column name after 'by'
            words = query_lower.split()
            if 'by' in words:
                by_index = words.index('by')
                if by_index + 1 < len(words):
                    group_col = words[by_index + 1]
                    # Check if this column exists
                    columns = [col['name'] for col in schema[table_name] ]
                    if group_col in columns:
                        return f"SELECT {group_col}, COUNT(*) as count FROM {table_name} GROUP BY {group_col} ORDER BY count DESC LIMIT 100"
        
        elif 'total' in query_lower or 'sum' in query_lower:
            # Find numeric column
            numeric_cols = [col['name'] for col in schema[table_name] 
                          if col['type'].upper() in ['INTEGER', 'REAL', 'NUMERIC', 'FLOAT']]
            if numeric_cols and 'by' in query_lower:
                words = query_lower.split()
                by_index = words.index('by')
                if by_index + 1 < len(words):
                    group_col = words[by_index + 1]
                    columns = [col['name'] for col in schema[table_name]]
                    if group_col in columns:
                        return f"SELECT {group_col}, SUM({numeric_cols[0]}) as total FROM {table_name} GROUP BY {group_col} ORDER BY total DESC LIMIT 100"
        
        # Default: return all
        return f"SELECT * FROM {table_name} LIMIT 100"
