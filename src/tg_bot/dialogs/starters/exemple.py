import logging

from aiogram import Router
from aiogram.filters import Command

from tg_bot import states
from tg_bot.utils.router import register_start_handler

logger = logging.getLogger(__name__)


def setup() -> Router:
    router = Router(name=__name__)
    register_start_handler(
        Command(commands="exemple"),
        state=states.ExempleSG.step_one,
        router=router,
    )
    return router
