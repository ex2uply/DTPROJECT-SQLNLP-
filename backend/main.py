from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db_manager import DBManager
from nlp_engine import NLPEngine
from reporting import ReportingModule

app = FastAPI(title="AI/ML Database Query System")

# Initialize modules
db_manager = DBManager()
nlp_engine = NLPEngine()
reporting_module = ReportingModule()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    sql: str
    results: List[Dict[str, Any]]
    chart_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI/ML Database Query System API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        # 1. Get Schema
        schema = db_manager.get_schema()
        
        # 2. Generate SQL
        sql = nlp_engine.generate_sql(request.query, schema)
        
        # 3. Execute SQL
        results = db_manager.execute_query(sql)
        
        # 4. Generate Report/Chart Data
        chart_data = reporting_module.generate_report(results)
        
        return {
            "sql": sql,
            "results": results,
            "chart_data": chart_data
        }
    except Exception as e:
        return {
            "sql": "",
            "results": [],
            "chart_data": None,
            "error": str(e)
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
