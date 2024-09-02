from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .api import router
from core.config import config
from core.exceptions import CustomException
# from core.utils.logger import LoggingMiddleware
from shared.logger import LoggingMiddleware
from core.fastapi.dependencies import validate_payload
from core.fastapi.middlewares import (
    CustomCORSMiddleware,
)

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(CustomCORSMiddleware),
        Middleware(LoggingMiddleware)
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Agri Bot Service",
        description="APIs related to Agri Bot",
        version="1.0.0",
        docs_url=None if config.ENVIRONMENT == "production" else "/agri_bot/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/agri_bot/redoc",
        dependencies=[Depends(validate_payload)],
        middleware=make_middleware(),
        openapi_url="/agri_bot/openapi.json"
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_

app = create_app()
