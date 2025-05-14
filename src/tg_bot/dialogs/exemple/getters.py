from aiogram_dialog import DialogManager


async def data_getter(dialog_manager: DialogManager, **kwargs):
    return {
        "first_name": dialog_manager.event.from_user.first_name,
    }
