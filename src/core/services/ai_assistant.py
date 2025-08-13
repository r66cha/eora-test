"""Модуль AI ассистента OpenAI."""

# -- Imports

import httpx
from openai import AsyncOpenAI
from src.core.config import settings

# -- Exports

__all__ = ["assistant"]

# --


class AssistantOpenAI:
    # TODO:  Сделать Docstring
    """Docstring"""

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
            # TODO:  Логировать ошибку
            return None

    async def process(self, msg: str) -> tuple:

        try:

            result: str = await self._set_gpt(msg)  # Получение ответа
            return result

        except Exception as e:
            # TODO:  Логировать ошибку
            return None


assistant = AssistantOpenAI()
