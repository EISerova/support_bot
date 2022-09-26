from unittest.mock import AsyncMock

import pytest

from handlers.echo import bot_echo
from settings.constants import ECHO_ANSWER


@pytest.mark.asyncio
async def test_echo_handler():
    text_mock = ECHO_ANSWER
    message_mock = AsyncMock(text=text_mock)
    await bot_echo(message=message_mock)
    message_mock.answer.assert_called_with(text_mock)
