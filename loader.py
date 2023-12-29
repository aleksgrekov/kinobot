from telebot import TeleBot

from config_data.config import ENVS

bot = TeleBot(token=ENVS.get('BOT_TOKEN'))
