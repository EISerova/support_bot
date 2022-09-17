from aiogram import types


async def set_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Написать сообщение в тех.поддержку"),
            types.BotCommand("help", "Помощь"),
        ]
    )
