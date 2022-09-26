from aiogram import Dispatcher

from settings import logging
from settings.config import ADMINS
from settings.constants import RUN_BOT_MESSAGE


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, RUN_BOT_MESSAGE)

        except Exception as error:
            logging.exception(error)
