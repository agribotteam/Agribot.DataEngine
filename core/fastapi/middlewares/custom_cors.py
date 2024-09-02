from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from core.config import config
from core.exceptions import ForbiddenException, UnauthorizedException
from starlette.middleware.base import BaseHTTPMiddleware

class CustomCORSMiddleware(BaseHTTPMiddleware):

     async def dispatch(self, request, call_next):

          logger.info(request.headers.get("Origin"))
          logger.info(request.client.host)

          if "*" not in config.ALLOW_ORIGINS_LIST:
               
               # Check the Origin header for CORS
               origin = request.headers.get("Origin")
               if origin and origin not in config.ALLOW_ORIGINS_LIST:
                    return JSONResponse(
                         status_code=UnauthorizedException.code,
                         content={"error_code": UnauthorizedException.code, "message": "CORS Policy Violation"},
                    )

               # Check the client IP address for IP filtering
               client_ip = request.client.host
               if client_ip not in config.ALLOW_ORIGINS_LIST:
                    return JSONResponse(
                         status_code=ForbiddenException.code,
                         content={"error_code": ForbiddenException.code, "message": ForbiddenException.message},
                    )

          response = await call_next(request)
          return response