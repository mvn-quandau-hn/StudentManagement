from fastapi import APIRouter
from pydantic import BaseModel
from app.service.rag_service import RagService

router = APIRouter(prefix="/rag", tags=["RAG QA"])

class Question(BaseModel):
    query: str

rag_service = RagService()
rag_service.load_model()

@router.post("/ask")
def ask_question(q: Question):
    return {"answer": rag_service.ask(q.query)}
