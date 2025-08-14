"""Модуль конфигурации приложения."""

# -- Imports

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.core.schemas import (
    ApiSchema,
    LoggingConfigSchema,
    RunConfigSchema,
    KeysSchema,
    AiAssistantDataSchema,
)

# -- Exports

__all__ = ["settings"]

# --

BASE_DIR = Path(__file__).resolve().parent.parent

# --


class Settings(BaseSettings):
    """Конфигурация приложения."""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(BASE_DIR / ".env"),  # env.dev
    )

    # --

    api: ApiSchema = ApiSchema()
    run: RunConfigSchema = RunConfigSchema()
    logging: LoggingConfigSchema = LoggingConfigSchema()

    # --

    keys: KeysSchema = KeysSchema()
    ai_assistant: AiAssistantDataSchema = AiAssistantDataSchema()


settings = Settings()
