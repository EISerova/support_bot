from aiogram import Dispatcher

from .support_middleware import SupportMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(SupportMiddleware())
