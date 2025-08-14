"""Модуль схемы EoraInfoSchema для парсера."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["EoraInfoSchema"]

# --


class EoraInfoSchema(BaseModel):
    """Парсинг схема."""

    case_: str
    description: str
