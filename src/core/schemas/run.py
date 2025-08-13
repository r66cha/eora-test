"""Configuration schemas for application runtime and Gunicorn server."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["RunConfigSchema"]

# --


class RunConfigSchema(BaseModel):
    """Configuration for running the application."""

    host: str = "0.0.0.0"
    port: int = 8000
