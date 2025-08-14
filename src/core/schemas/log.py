"""Модуль схемы логирования."""

# -- Imports

import logging
from typing import Literal
from pydantic import BaseModel

# -- Exports

__all__ = ["LoggingConfigSchema"]

# --


LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)3s:%(lineno)-3d %(levelname)-3s - %(message)s"
)


class LoggingConfigSchema(BaseModel):
    """Схема настройки уровня и формата логирования."""

    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"

    log_format: str = LOG_DEFAULT_FORMAT

    @property
    def log_level_value(self) -> int:
        """Преобразует уровень строкового значения в соответствующую числовую константу.."""

        return logging.getLevelNamesMapping()[self.log_level.upper()]
