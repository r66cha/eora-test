"""Модуль конфигурации Proxy."""

# -- Imports

from pydantic_settings import BaseSettings, SettingsConfigDict

# -- Exports

__all__ = ["proxy_config"]

# --


class ProxyConfig(BaseSettings):
    # TODO: Docstring

    model_config = SettingsConfigDict(
        env_file=".env",  # env.example
        extra="ignore",
    )

    PROXY: str

    @property
    def get_PROXY(self) -> str:
        return self.PROXY


proxy_config = ProxyConfig()
