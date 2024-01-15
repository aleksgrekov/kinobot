from telebot import custom_filters
import handlers

from loader import bot
from utils.set_bot_commands import set_default_commands
from database.models import create_models

if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    create_models()
    set_default_commands(bot)
    bot.infinity_polling()
