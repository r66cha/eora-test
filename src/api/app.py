"""FastAPI application instance."""

# -- Imports

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .description import title, description, version
from src.api.routers._0_main_router import main_router
from fastapi.responses import ORJSONResponse


log = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        default_response_class=ORJSONResponse,
        docs_url="/docs",
    )

    # Routers
    app.include_router(main_router)

    # Middleware
    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=["*"],
    )

    return app


app = create_app()
