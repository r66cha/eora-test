"""Модуль AI ассистента OpenAI."""

# -- Imports

import httpx
import logging
from openai import AsyncOpenAI
from src.core.config import settings

# -- Exports

__all__ = ["assistant", "get_assistant"]

# --

log = logging.getLogger(__name__)
logging.basicConfig(
    level=settings.logging.log_level_value,
    format=settings.logging.log_format,
)

# --


class AssistantOpenAI:
    """Класс ассистента OpenAI"""

    def __init__(self):
        self.proxy = settings.keys.PROXY
        self.api_key = settings.keys.OPENAI_API_KEY

        self.transport = httpx.AsyncHTTPTransport(proxy=self.proxy)
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            http_client=httpx.AsyncClient(transport=self.transport),
        )

    async def _set_gpt(
        self,
        msg: str,
        model: str = settings.ai_assistant.model,
    ):

        try:

            completion = await self.client.chat.completions.create(
                model=model,
                max_tokens=500,
                seed=1,
                messages=[
                    {
                        "role": "system",
                        "content": settings.ai_assistant.eora_assistant_content,
                    },
                    {
                        "role": "user",
                        "content": msg,
                    },
                ],
            )
            return completion.choices[0].message.content

        except Exception as e:
            log.error(f"Error as: {e}")
            return None

    async def process(self, msg: str) -> tuple:

        try:

            result: str = await self._set_gpt(msg)
            log.info(f"Result from gpt: {result}")
            return result

        except Exception as e:
            log.error(f"Error as: {e}")
            return None


assistant = AssistantOpenAI()

# --


# Для Depends
async def get_assistant():
    return assistant
