from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


async def text_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
) -> None:
    await message.reply("Yes, it is really not interesting. Bye Bye!\n /exemple")
    await manager.done()


async def other_type_handler(
    message: Message,
    message_input: MessageInput,
    manager: DialogManager,
) -> None:
    await message.answer("Text is expected")
