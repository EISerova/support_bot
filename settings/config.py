from environs import Env, EnvError
import logging

from settings.constants import ERROR_TOKEN


env = Env()
env.read_env()

try:
    BOT_TOKEN = env.str("BOT_TOKEN")
    ADMINS = env.list("ADMINS")
    FIRST_OPERATOR = env.str("FIRST_OPERATOR")
    SECOND_OPERATOR = env.str("SECOND_OPERATOR")
except EnvError as error:
    logging.critical(ERROR_TOKEN.format(error=error), exc_info=True)
    exit(1)

OPERATOR_IDS = [FIRST_OPERATOR, SECOND_OPERATOR]
OPERATOR_LOGINS = {FIRST_OPERATOR: 'FIRST_OPERATOR', SECOND_OPERATOR: 'SECOND_OPERATOR'}
