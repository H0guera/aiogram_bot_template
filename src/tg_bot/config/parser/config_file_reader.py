import yaml

from tg_bot.config.models import Paths


def read_config(paths: Paths) -> dict:
    with (paths.config_path / "config.yml").open("r") as f:
        return yaml.safe_load(f)
