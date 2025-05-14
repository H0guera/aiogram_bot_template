import logging

from aiogram import Dispatcher
from aiogram_dialog.api.protocols import MessageManagerProtocol
from aiogram_dialog.manager.message_manager import MessageManager
from dishka import AsyncContainer, Provider, Scope, make_async_container, provide
from dishka.integrations.aiogram import setup_dishka

from infrastructure.di import get_providers
from tg_bot.handlers import setup_handlers
from tg_bot.utils.router import print_router_tree

logger = logging.getLogger(__name__)


def create_dishka(path_env: str) -> AsyncContainer:
    return make_async_container(*get_bot_providers(path_env))


def get_bot_providers(path_env: str) -> list[Provider]:
    return [
        *get_providers(path_env),
        *get_bot_specific_providers(),
    ]


def get_bot_specific_providers() -> list[Provider]:
    return [
        DpProvider(),
        DialogManagerProvider(),
    ]


class DialogManagerProvider(Provider):
    scope = Scope.APP

    @provide
    def get_manager(self) -> MessageManagerProtocol:
        return MessageManager()


class DpProvider(Provider):
    scope = Scope.APP

    @provide
    def create_dispatcher(
        self,
        dishka: AsyncContainer,
    ) -> Dispatcher:
        dp = Dispatcher()
        setup_dishka(container=dishka, router=dp)
        setup_handlers(dp)
        logger.info("Configured bot routers \n%s", print_router_tree(dp))

        return dp


def resolve_update_types(dp: Dispatcher) -> list[str]:
    return dp.resolve_used_update_types(skip_events={"aiogd_update"})
