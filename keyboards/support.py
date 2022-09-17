import random

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from loader import dp
from settings.config import operator_ids
from settings.constants import END_BUTTON, SUPPORT_ANSWER_BUTTON, USER_QUESTION_BUTTON

support_callback = CallbackData("ask_support", "messages", "operator_id", "is_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")


async def check_operator_status(operator_id):
    """
    Проверяет статус оператора,
    если in_support - оператор занят.
    """
    state = dp.current_state(chat=operator_id, user=operator_id)
    state_str = str(await state.get_state())
    if state_str == "in_support":
        return
    return operator_id


async def get_operator():
    # random.shuffle(support_ids)
    for operator_id in operator_ids:
        # Проверим если оператор в данное время не занят
        operator_id = await check_operator_status(operator_id)
        return operator_id


async def support_keyboard(messages, user_id=None):
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
        if messages == "many" and contact_id is None:
            # Если не нашли свободного оператора - выходим и говорим, что его нет
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(operator_ids)

    keyboard = InlineKeyboardMarkup()

    ask_button = InlineKeyboardButton(
        text=text,
        callback_data=support_callback.new(
            messages=messages, operator_id=contact_id, is_user=is_user
        ),
    )

    end_button = InlineKeyboardButton(
        text=END_BUTTON, callback_data=cancel_support_callback.new(user_id=contact_id)
    )

    if messages == "many":
        buttons = [ask_button, end_button]
    else:
        buttons = [ask_button]

    keyboard.add(*buttons)
    return keyboard


def cancel_support(user_id):
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
