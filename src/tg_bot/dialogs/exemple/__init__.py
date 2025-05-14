from aiogram import Router

from .dialog import exemple


def setup(router: Router) -> None:
    router.include_router(exemple)
