import asyncio
import logging

from aiogram import Bot, Dispatcher

from tg_bot.config.parser.logging_config import setup_logging
from tg_bot.config.parser.paths import get_paths
from tg_bot.main_factory import create_dishka, resolve_update_types

logger = logging.getLogger(__name__)


async def main() -> None:
    paths = get_paths("BOT_PATH")
    setup_logging(paths)
    dishka = create_dishka("BOT_PATH")
    dp = await dishka.get(Dispatcher)
    bot = await dishka.get(Bot)

    try:
        await bot.delete_webhook()
        await dp.start_polling(bot, allowed_updates=resolve_update_types(dp))

    finally:
        logger.info("stopped")
        await dishka.close()


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
