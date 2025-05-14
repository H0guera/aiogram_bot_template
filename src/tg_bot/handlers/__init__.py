import logging

from aiogram import Dispatcher

from tg_bot.handlers import base

logger = logging.getLogger(__name__)


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(base.setup())
    logger.debug("handlers configured successfully")
