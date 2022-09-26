import logging

import handlers
from loader import dp
from settings.commands import set_commands
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    import middlewares

    middlewares.setup(dp)
    await set_commands(dp)
    await on_startup_notify(dp)


if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)

else:
    log = logging.getLogger(__name__)
