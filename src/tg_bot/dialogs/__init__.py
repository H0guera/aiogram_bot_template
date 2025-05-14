from aiogram import F, Router
from aiogram.enums import ChatType
from aiogram_dialog import setup_dialogs
from aiogram_dialog.api.protocols import MessageManagerProtocol

from tg_bot.dialogs import exemple, starters


def setup(router: Router, message_manager: MessageManagerProtocol) -> None:
    dialog_router = Router(name=__name__)
    dialog_router.message.filter(F.chat.type == ChatType.PRIVATE)

    dialog_router.include_router(starters.setup())
    dialog_router.include_router(setup_all_dialogs())

    setup_dialogs(dialog_router, message_manager=message_manager)
    router.include_router(dialog_router)


def setup_all_dialogs() -> Router:
    router = Router(name=__name__ + ".common")

    exemple.setup(router)
    return router
