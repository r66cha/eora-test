"""Модуль роутеров для пользователя."""

# -- Imports

import logging
from fastapi import (
    APIRouter,
    status,
    HTTPException,
    Depends,
    Body,
)

from src.core.services import get_assistant
from src.core.config import settings
from dotenv import load_dotenv

load_dotenv()


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.services.ai_assistant import AssistantOpenAI


# --

log = logging.getLogger(__name__)
logging.basicConfig(
    level=settings.logging.log_level_value,
    format=settings.logging.log_format,
)

# --

user_router = APIRouter(
    prefix=settings.api.chat,
    tags=["Chat"],
)

# --


# Eora-Chat endpoint
@user_router.post(
    "/",
    status_code=status.HTTP_200_OK,
    name="Eora-Chat",
)
async def set_info_about_me(
    assistant: "AssistantOpenAI" = Depends(get_assistant),
    data: dict = Body(
        ...,
        example={"User": {"message": "А что вы делали для интернет магазинов одежды?"}},
    ),
):
    """В этом роутере напишите свой вопрос ассистенту как показано в примере."""

    try:

        msg = data.get("User", {"Message": "Hello"}).get("message", "")
        res = await assistant.process(msg)
        return {"Ассистент EORA": res}

    except HTTPException as e:
        log.error(f"Exception: {e}")
