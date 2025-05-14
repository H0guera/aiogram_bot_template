import logging

from aiogram import Dispatcher
from aiogram_dialog.api.protocols import MessageManagerProtocol

from tg_bot import dialogs
from tg_bot.handlers import base

logger = logging.getLogger(__name__)


def setup_handlers(dp: Dispatcher, message_manager: MessageManagerProtocol) -> None:
    dialogs.setup(dp, message_manager)

    dp.include_router(base.setup())
    logger.debug("handlers configured successfully")
