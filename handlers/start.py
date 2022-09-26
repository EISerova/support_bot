import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.support import (
    cancel_support,
    cancel_support_callback,
    support_callback,
    support_keyboard,
)
from loader import bot, dp
from settings.constants import (
    END_DIALOG,
    END_DIALOG_FOR_USER_MESSAGE,
    NO_FREE_OPERATORS_MESSAGE,
    OPERATOR_END_DIALOG_MESSAGE,
    START_DIALOG_OPERATOR,
    START_DIALOG_USER,
    START_DIALOG_WITH_OPERATOR_MESSAGE,
    START_DIALOG_WITH_USER_MESSAGE,
    START_GREETING_MESSAGE,
    USER_GET_START,
    USER_REFUSE_MESSAGE,
    USER_REQUEST_MESSAGE,
    WAIT_FOR_OPERATOR_MESSAGE,
    WAIT_OPERATOR_MESSAGE,
)
from utils.get_operators import check_operator_status, get_operator


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """Хэндлер для команды /start."""
    logging.info(USER_GET_START.format(user=message.from_user.id))
    keyboard = await support_keyboard()
    try:
        await message.answer(START_GREETING_MESSAGE, reply_markup=keyboard)
    except Exception as error:
        logging.exception(error)


@dp.message_handler(state="wait_for_support", content_types=types.ContentTypes.ANY)
async def not_supported(message: types.Message, state: FSMContext):
    """Хэндлер для юзера в состоянии wait_for_support."""
    data = await state.get_data()
    user = data.get("user_id")
    try:
        await message.answer(
            WAIT_FOR_OPERATOR_MESSAGE, reply_markup=cancel_support(user)
        )
    except Exception as error:
        logging.exception(error)


@dp.callback_query_handler(support_callback.filter(is_user="yes"))
async def send_to_support_call(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    """Хэндлер для юзера."""

    try:
        await call.message.edit_text(
            WAIT_OPERATOR_MESSAGE, reply_markup=cancel_support(call.from_user.id)
        )
    except Exception as error:
        logging.exception(error)

    operator_id = int(callback_data.get("user_id"))
    if not await check_operator_status(operator_id):
        operator = await get_operator()
    else:
        operator = operator_id

    if not operator:
        try:
            await call.message.edit_text(NO_FREE_OPERATORS_MESSAGE)
            await state.reset_state()
        except Exception as error:
            logging.exception(error)
        return

    keyboard = await support_keyboard(user_id=call.from_user.id)
    await state.set_state("wait_for_support")
    await state.update_data(user_id=operator)
    logging.info(START_DIALOG_USER.format(chat_instance=call.message["chat"]))
    await bot.send_message(
        operator,
        USER_REQUEST_MESSAGE.format(user=call.from_user.full_name),
        reply_markup=keyboard,
    )


@dp.callback_query_handler(support_callback.filter(is_user="no"))
async def start_dialog_with_user(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    """Хэндлер для оператора."""
    user = int(callback_data.get("user_id"))
    user_state = dp.current_state(user=user, chat=user)

    if str(await user_state.get_state()) != "wait_for_support":
        try:
            await call.message.edit_text(USER_REFUSE_MESSAGE)
        except Exception as error:
            logging.exception(error)
        return
    logging.info(
        START_DIALOG_OPERATOR.format(chat_instance=call.message["chat"]["username"])
    )
    await state.set_state("in_support")
    await user_state.set_state("in_support")
    await state.update_data(user_id=user)
    try:
        await call.message.edit_text(
            START_DIALOG_WITH_USER_MESSAGE, reply_markup=cancel_support(user)
        )
        await bot.send_message(
            user,
            START_DIALOG_WITH_OPERATOR_MESSAGE,
        )
    except Exception as error:
        logging.exception(error)


@dp.callback_query_handler(
    cancel_support_callback.filter(), state=["in_support", "wait_for_support", None]
)
async def exit_support(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    """Завершение чата."""
    user_id = int(callback_data.get("user_id"))
    current_state = dp.current_state(user=user_id, chat=user_id)

    if await current_state.get_state():
        await current_state.reset_state()
        logging.info(
            END_DIALOG.format(user=user_id, chat_instance=call.message["chat"])
        )
        await bot.send_message(user_id, END_DIALOG_FOR_USER_MESSAGE)

    try:
        await call.message.edit_text(OPERATOR_END_DIALOG_MESSAGE)
        await state.reset_state()
    except Exception as error:
        logging.exception(error)
