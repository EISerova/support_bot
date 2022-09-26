import os

import pytest


def test_env():
    ENV_VARS = ["ADMINS", "BOT_TOKEN", "OPERATOR_IDS"]

    for var in ENV_VARS:
        try:
            os.environ.pop(var)
        except KeyError as error:
            for arg in error.args:
                if arg in ENV_VARS:
                    assert False, (
                        "Проверьте, наличие необходимых переменных окружения"
                        f" {repr(error)}"
                    )
