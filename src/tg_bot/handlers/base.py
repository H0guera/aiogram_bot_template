from aiogram import Router
from aiogram.types import Message


async def echo(message: Message) -> None:
    if message.text:
        await message.reply(message.text)


def setup() -> Router:
    router = Router(name=__name__)
    router.message.register(echo)
    return router
