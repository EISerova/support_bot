import random
from loader import dp
from settings.config import OPERATOR_IDS


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
    """
    Рандомный выбор оператора из списка OPERATOR_IDS.
    Дополнительная проверка check_operator_status, что оператор не занят.
    """
    random.shuffle(OPERATOR_IDS)
    for operator_id in OPERATOR_IDS:
        operator_id = await check_operator_status(operator_id)
        if operator_id:
            return operator_id
    else:
        return
