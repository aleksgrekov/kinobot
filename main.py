from loader import bot
from utils.set_bot_commands import set_default_commands
from database.models import create_models

import handlers

if __name__ == "__main__":
    create_models()
    set_default_commands(bot)
    bot.infinity_polling()
