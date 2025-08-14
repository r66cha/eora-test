"""Модуль конфигурации схемы для построения путей к конечным точкам API.."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["ApiSchema"]

# --


class ApiSchema(BaseModel):
    """Схема конфигурации для конечных точек базового API."""

    prefix: str = "/eora"
    chat: str = "/chat"

    @property
    def set_data_url(self) -> str:
        """Full path for set data route."""

        return f"{self.prefix}{self.chat}"
