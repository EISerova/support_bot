import logging
import random
import typing

from loader import dp
from settings.config import OPERATOR_IDS, OPERATOR_LOGINS
from settings.constants import GET_OPERATOR, NO_FREE_OPERATORS


async def check_operator_status(operator_id) -> typing.Union[int, None]:
    """
    Проверяет статус оператора,
    если in_support - оператор занят.
    """
    state = dp.current_state(chat=operator_id, user=operator_id)
    state_str = str(await state.get_state())
    if state_str == "in_support":
        return
    return operator_id


async def get_operator() -> typing.Union[int, None]:
    """
    Рандомный выбор оператора из списка OPERATOR_IDS.
    Дополнительная проверка check_operator_status, что оператор не занят.
    """
    checked_operators = {}
    random.shuffle(OPERATOR_IDS)
    for operator_id in OPERATOR_IDS:
        checked_id = await check_operator_status(operator_id)
        checked_operators[operator_id] = checked_id
        if checked_id:
            operator_name = OPERATOR_LOGINS.get(checked_id)
            logging.info(GET_OPERATOR.format(operator_name=operator_name))
            return operator_id
    else:
        logging.info(NO_FREE_OPERATORS.format(checked_operators=checked_operators))
        return
