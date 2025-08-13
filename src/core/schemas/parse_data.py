"""Модуль схемы EoraInfoSchema для парсера."""

# -- Imports

from pydantic import BaseModel

# -- Exports

__all__ = ["EoraInfoSchema"]

# --


class EoraInfoSchema(BaseModel):
    # TODO: Docstring
    """Docstring"""

    case_: str
    description: str
