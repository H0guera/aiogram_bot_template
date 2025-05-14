from dataclasses import dataclass
from pathlib import Path

from tg_bot.config.models import BotConfig, Paths


@dataclass
class Config:
    paths: Paths
    bot: BotConfig

    @property
    def app_dir(self) -> Path:
        return self.paths.app_dir

    @property
    def config_path(self) -> Path:
        return self.paths.config_path

    @property
    def log_path(self) -> Path:
        return self.paths.log_path
