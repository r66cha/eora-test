"""Входная точка в приложение используя веб-сервер Uvicorn."""

# -- Imports

import uvicorn
from src.core.config import settings
from src.api.app import app

# --

# Entry point
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
