from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    log_chat: int
    superusers: list[int]
