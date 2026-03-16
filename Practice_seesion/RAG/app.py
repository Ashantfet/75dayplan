from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import rag_pipeline

app = FastAPI(title="Production RAG API")

class QueryRequest(BaseModel):
    query: str
    role: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    return rag_pipeline(request.query, request.role)

@app.get("/")
def root():
    return {"message": "RAG API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
