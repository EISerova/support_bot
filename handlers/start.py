from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.support import (
    cancel_support,
    cancel_support_callback,
    check_operator_status,
    get_operator,
    support_callback,
    support_keyboard,
)
from loader import bot, dp
from settings.constants import (
    NO_FREE_OPERATORS_MESSAGE,
    OPERATOR_END_DIALOG,
    START_DIALOG_WITH_OPERATOR_MESSAGE,
    START_DIALOG_WITH_USER_MESSAGE,
    START_GREETING_MESSAGE,
    USER_END_DIALOG,
    USER_REFUSE_MESSAGE,
    USER_REQUEST_MESSAGE,
    WAIT_FOR_OPERATOR_MESSAGE,
    WAIT_OPERATOR_MESSAGE,
)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """
    Действия при команде /start.

    """
    keyboard = await support_keyboard(messages="many")
    if not keyboard:
        await message.answer(NO_FREE_OPERATORS_MESSAGE)
        return
    await message.answer(START_GREETING_MESSAGE, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages="many", is_user="yes"))
async def send_to_support_call(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    await call.message.edit_text(WAIT_OPERATOR_MESSAGE)

    operator_id = int(callback_data.get("operator_id"))

    if not operator_id:
        await call.message.edit_text(NO_FREE_OPERATORS_MESSAGE)
        await state.reset_state()
        return

    if not await check_operator_status(operator_id):
        operator = await get_operator()
    else:
        operator = operator_id

    await state.set_state("wait_for_support")
    await state.update_data(operator_id=operator)

    keyboard = await support_keyboard(messages="many", user_id=call.from_user.id)

    if call.from_user.full_name:
        await bot.send_message(
            operator,
            USER_REQUEST_MESSAGE.format(user=call.from_user.full_name),
            reply_markup=keyboard,
        )
    else:
        await bot.send_message(
            operator,
            USER_REQUEST_MESSAGE.format(user=call.from_user.id),
            reply_markup=keyboard,
        )


@dp.callback_query_handler(support_callback.filter(messages="many", is_user="no"))
async def start_dialog_with_user(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    operator_id = int(callback_data.get("operator_id"))
    user_state = dp.current_state(user=operator_id, chat=operator_id)

    if str(await user_state.get_state()) != "wait_for_support":
        await call.message.edit_text(USER_REFUSE_MESSAGE)
        return

    await state.set_state("in_support")
    await user_state.set_state("in_support")

    await state.update_data(operator_id=operator_id)

    keyboard = cancel_support(operator_id)
    keyboard_second_user = cancel_support(call.from_user.id)

    await call.message.edit_text(START_DIALOG_WITH_USER_MESSAGE, reply_markup=keyboard)
    await bot.send_message(
        operator_id,
        START_DIALOG_WITH_OPERATOR_MESSAGE,
        reply_markup=keyboard_second_user,
    )


@dp.message_handler(state="wait_for_support", content_types=types.ContentTypes.ANY)
async def not_supported(message: types.Message, state: FSMContext):
    data = await state.get_data()
    operator_id = data.get("operator_id")

    keyboard = cancel_support(operator_id)
    await message.answer(WAIT_FOR_OPERATOR_MESSAGE, reply_markup=keyboard)


@dp.callback_query_handler(
    cancel_support_callback.filter(), state=["in_support", "wait_for_support", None]
)
async def exit_support(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    user_id = int(callback_data.get("user_id"))
    second_state = dp.current_state(user=user_id, chat=user_id)

    if await second_state.get_state() is not None:
        data_second = await second_state.get_data()
        operator_id = data_second.get("operator_id")
        if int(operator_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, USER_END_DIALOG)

    await call.message.edit_text(OPERATOR_END_DIALOG)
    await state.reset_state()
