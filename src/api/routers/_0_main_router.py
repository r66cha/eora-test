"""Main app router"""

# -- Imports

from fastapi import APIRouter, Depends
from src.core.config import settings
from src.api.routers.user_router import user_router


# --

main_router = APIRouter(prefix=settings.api.prefix)
main_router.include_router(user_router)
