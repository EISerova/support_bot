import logging

from aiogram import types

from loader import dp
from settings.constants import ECHO_ANSWER


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(ECHO_ANSWER)
    logging.info(
        f'Запрос "{message.text}" от юзера {message.from_user.id} в состоянии state=None'
    )
