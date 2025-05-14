from dishka import Provider
from dishka.integrations.aiogram import AiogramProvider

from infrastructure.di.bot import BotProvider
from infrastructure.di.config import ConfigProvider


def get_providers(path_env: str) -> list[Provider]:
    return [
        ConfigProvider(path_env),
        BotProvider(),
        AiogramProvider(),
    ]
