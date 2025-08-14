"""Модуль Конфигурации подключения к OpenAI API."""

# -- Imports

from pydantic_settings import BaseSettings, SettingsConfigDict

# -- Exports

__all__ = ["open_ai_config"]

# --


class OpenAIConnectionConfig(BaseSettings):
    """Класс схемы настройки подключения к OpenAI API."""

    model_config = SettingsConfigDict(
        env_file=".env",  # env.dev
        extra="ignore",
    )

    OPENAI_API_KEY: str

    @property
    def get_OPENAI_API_KEY(self) -> str:
        return self.OPENAI_API_KEY


open_ai_config = OpenAIConnectionConfig()
