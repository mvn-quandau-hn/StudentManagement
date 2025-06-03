from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import json

def format_response(success: bool, error: str = "", data=None):
    return {
        "success": success,
        "error": error,
        "data": data
    }

class ResponseFormatterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        if response.status_code >= 400:
            return response  

        if "application/json" in response.headers.get("content-type", ""):
            raw_body = [section async for section in response.body_iterator]
            body = b"".join(raw_body).decode()
            try:
                data = json.loads(body)
            except Exception:
                data = body

            new_response = JSONResponse(
                content=format_response(True, data=data),
                status_code=response.status_code
            )
            return new_response

        return response
