from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

class APIException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

def format_response(success: bool, error: str = "", data=None):
    return {
        "success": success,
        "error": error,
        "data": data
    }

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=format_response(False, error=exc.detail)
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]['msg'] if exc.errors() else "Validation error"
    return JSONResponse(
        status_code=422,
        content=format_response(False, error=first_error)
    )

async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=format_response(False, error=exc.message)
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=format_response(False, error="Internal Server Error")
    )
