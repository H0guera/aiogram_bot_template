from collections.abc import AsyncIterable

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import Provider, Scope, provide

from tg_bot.config.models import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_bot(self, config: BotConfig) -> AsyncIterable[Bot]:
        async with Bot(
            token=config.token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
        ) as bot:
            yield bot
