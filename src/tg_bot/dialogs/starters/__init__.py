from aiogram import F, Router
from aiogram.enums import ChatType

from . import exemple


def setup() -> Router:
    router = Router(name=__name__)
    router.message.filter(F.chat.type == ChatType.PRIVATE)
    router.include_router(exemple.setup())
    return router
