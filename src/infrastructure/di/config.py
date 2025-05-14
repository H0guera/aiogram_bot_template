from dishka import Provider, Scope, provide

from tg_bot.config.models import BotConfig, Paths
from tg_bot.config.models.main import Config
from tg_bot.config.parser.main import load_config
from tg_bot.config.parser.paths import get_paths


class ConfigProvider(Provider):
    scope = Scope.APP

    def __init__(self, path_env: str = "BOT_PATH") -> None:
        super().__init__()
        self.path_env = path_env

    @provide
    def get_paths(self) -> Paths:
        return get_paths(self.path_env)

    @provide
    def get_config(self, paths: Paths) -> Config:
        return load_config(paths)

    @provide
    def get_bot_config(self, config: Config) -> BotConfig:
        return config.bot
