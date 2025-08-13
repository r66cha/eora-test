"""Schema configuration for constructing API endpoint paths."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["ApiSchema"]

# --


class ApiSchema(BaseModel):
    """Configuration schema for base API endpoints."""

    prefix: str = "/eora"
    chat: str = "/chat"

    @property
    def set_data_url(self) -> str:
        """Full path for set data route."""

        return f"{self.prefix}{self.chat}"
