from fastapi import APIRouter
from pydantic import BaseModel
from app.service.rag_service import rag_service

router = APIRouter(prefix="/rag", tags=["RAG QA"])

class Question(BaseModel):
    query: str

@router.post("/ask")
def ask_question(q: Question):
    return {"answer": rag_service.ask(q.query)}
