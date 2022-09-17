# import os
# from dotenv import load_dotenv
# load_dotenv()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# OPERATORS_IDS =  os.getenv("OPERATORS_IDS")

from environs import Env


# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
OPERATOR_IDS = env.str('OPERATOR_IDS').split(',')
