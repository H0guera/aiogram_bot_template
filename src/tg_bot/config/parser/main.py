from tg_bot.config.models import BotConfig, Paths
from tg_bot.config.models.main import Config

from .config_file_reader import read_config


def load_config(paths: Paths) -> Config:
    config_dct = read_config(paths)
    return Config(
        paths=paths,
        bot=load_bot_config(config_dct["bot"]),
    )


def load_bot_config(dct: dict) -> BotConfig:
    return BotConfig(
        token=dct["token"],
        log_chat=dct["log-chat"],
        superusers=dct["superusers"],
    )
