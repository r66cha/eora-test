"""Модуль схем ключей подключения."""

# -- Imports

from pydantic import BaseModel
from src.core.settings import open_ai_config, proxy_config

# -- Exports

__all__ = ["KeysSchema"]

# --


class KeysSchema(BaseModel):
    """Схема ключей для подключения к OpenAI API и Proxy."""

    OPENAI_API_KEY: str = open_ai_config.get_OPENAI_API_KEY
    PROXY: str = proxy_config.get_PROXY
