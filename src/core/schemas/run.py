"""Схемы конфигурации для среды выполнения приложений и сервера Uvicorn."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["RunConfigSchema"]

# --


class RunConfigSchema(BaseModel):
    """Схема конфигурации API."""

    host: str = "0.0.0.0"
    port: int = 8000
