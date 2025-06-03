from fastapi import FastAPI
from app.api import student_router
from app.db.database import create_db_and_tables
from app.middlewares.response_formatter import ResponseFormatterMiddleware
from app.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    api_exception_handler,
    generic_exception_handler,
    APIException
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()
app.add_middleware(ResponseFormatterMiddleware)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(student_router.router)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

