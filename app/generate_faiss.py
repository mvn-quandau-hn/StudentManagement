from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from app.extract_data import extract_documents
from app.db.database import SessionLocal
import os

def generate_faiss_index():
    with SessionLocal() as session:
        docs_text = extract_documents(session)
        if not docs_text:
            return False

    docs = [Document(page_content=txt) for txt in docs_text]
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local("faiss_index")
