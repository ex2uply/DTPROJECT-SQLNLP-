import pandas as pd
from typing import List, Dict, Any

class ReportingModule:
    def __init__(self):
        pass

    def generate_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze data and suggest chart configurations.
        """
        if not data:
            return {}
            
        df = pd.DataFrame(data)
        
        # Simple heuristic for chart type
        chart_type = "table"
        x_axis = None
        y_axis = None
        
        if len(df) > 0:
            # If we have a date column and a numeric column, suggest a line chart
            date_cols = [col for col in df.columns if 'date' in col.lower()]
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            
            if date_cols and numeric_cols:
                chart_type = "line"
                x_axis = date_cols[0]
                y_axis = numeric_cols[0]
            elif len(df) < 20 and len(numeric_cols) > 0:
                # If few rows, maybe a bar chart
                chart_type = "bar"
                # Try to find a categorical column for X
                cat_cols = df.select_dtypes(include=['object']).columns.tolist()
                if cat_cols:
                    x_axis = cat_cols[0]
                    y_axis = numeric_cols[0]

        return {
            "type": chart_type,
            "x_axis": x_axis,
            "y_axis": y_axis,
            "title": "Generated Report"
        }
