import os
from pathlib import Path

from tg_bot.config.models import Paths


def get_paths(env_var: str) -> Paths:
    if path := os.getenv(env_var):
        return Paths(Path(path))
    return Paths(Path(__file__).parent.parent.parent.parent.parent)
