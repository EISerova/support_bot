import random

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from settings.config import OPERATOR_IDS
from settings.constants import END_BUTTON, SUPPORT_ANSWER_BUTTON, USER_QUESTION_BUTTON
from utils.get_operators import get_operator

support_callback = CallbackData("ask_support", "user_id", "is_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")


async def support_keyboard(user_id=None):
    """
    Клавиатура запроса в тех.поддержку.
    Если user_id указан - меню для оператора,
    если user_id не указан - меню пользователя.
    """

    if user_id:
        is_user = "no"
        contact_id = int(user_id)
        text = SUPPORT_ANSWER_BUTTON

    else:
        contact_id = await get_operator()
        is_user = "yes"
        text = USER_QUESTION_BUTTON
        if contact_id is None:
            contact_id = random.choice(OPERATOR_IDS)

    keyboard = InlineKeyboardMarkup()

    ask_button = InlineKeyboardButton(
        text=text,
        callback_data=support_callback.new(user_id=contact_id, is_user=is_user),
    )

    end_button = InlineKeyboardButton(
        text=END_BUTTON, callback_data=cancel_support_callback.new(user_id=contact_id)
    )

    keyboard.add(ask_button, end_button)
    return keyboard


def cancel_support(user_id):
    """Клавиатура завершения чата."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=END_BUTTON,
                    callback_data=cancel_support_callback.new(user_id=user_id),
                )
            ]
        ]
    )
