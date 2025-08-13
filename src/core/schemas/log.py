"""Logging configuration schema"""

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
    """Schema for configuring logging level and format."""

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
        """Converts string log level to corresponding numeric constant."""

        return logging.getLevelNamesMapping()[self.log_level.upper()]
