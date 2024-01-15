from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data.config import ENVS

state_storage = StateMemoryStorage()
bot = TeleBot(token=ENVS.get('BOT_TOKEN'), state_storage=state_storage)
