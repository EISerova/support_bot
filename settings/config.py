# import os
# from dotenv import load_dotenv
# load_dotenv()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# OPERATORS_IDS =  os.getenv("OPERATORS_IDS")

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


# telegram-id сотрудников службы поддержки.
operator_ids = [
    147956065,
]
