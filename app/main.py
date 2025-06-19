from fastapi import FastAPI
from app.api import student_router, grade_router, subject_router
import os
from app.api.rag_router import router as rag_router
from app.db.database import create_db_and_tables,SessionLocal
from app.middlewares.response_formatter import ResponseFormatterMiddleware
from app.generate_faiss import generate_faiss_index
from app.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    api_exception_handler,
    generic_exception_handler,
    APIException
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.service.rag_service import rag_service



app = FastAPI()
app.add_middleware(ResponseFormatterMiddleware)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    if not os.path.exists("faiss_index/index.faiss"):
        print("Chưa có FAISS index, tạo mới...")
        from app.generate_faiss import generate_faiss_index
        generate_faiss_index()
    else:
        print("Đã có FAISS index, load model...")
        rag_service.load_model()

app.include_router(student_router.router)
app.include_router(grade_router.router)
app.include_router(subject_router.router)
app.include_router(rag_router)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

