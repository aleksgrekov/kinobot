from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data.config import ENVS

"""
Модуль, содержащий настройки для загрузки бота и хранилища состояний.

Переменные:
- state_storage: Экземпляр StateMemoryStorage для хранения состояний бота.
- bot: Экземпляр TeleBot, созданный с использованием токена из переменных окружения и указанным хранилищем состояний.

"""

state_storage = StateMemoryStorage()
bot = TeleBot(token=ENVS.get('BOT_TOKEN'), state_storage=state_storage)
