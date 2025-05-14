from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const, Format

from tg_bot import states

from .getters import data_getter
from .handlers import other_type_handler, text_handler

exemple = Dialog(
    Window(
        Format("Greetings, {first_name}, you see exemple of dialog"),
        Next(Const("Next")),
        getter=data_getter,
        state=states.ExempleSG.step_one,
    ),
    Window(
        Const("Now text me something"),
        MessageInput(text_handler, content_types=[ContentType.TEXT]),
        MessageInput(other_type_handler),
        state=states.ExempleSG.step_two,
    ),
)
