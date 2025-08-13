"""User Routers module."""

# -- Imports

import logging
from fastapi import (
    APIRouter,
    status,
    Request,
    Response,
    UploadFile,
    HTTPException,
    Depends,
    Header,
    Body,
    Form,
    Cookie,
    File,
)

from src.core.config import settings
from dotenv import load_dotenv

load_dotenv()


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


# Eora-Chat endpoint | (REST) | Without webhook
@user_router.post(
    "/",
    status_code=status.HTTP_200_OK,
    name="Eora-Chat",
)
async def set_info_about_me(
    data: dict = Body(
        ...,
        example={"User": {"message": "А что вы делали для интернет магазинов одежды?"}},
    )
):
    """Router for chat"""

    return {"received": data}
