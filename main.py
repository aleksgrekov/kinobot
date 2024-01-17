from telebot.custom_filters import StateFilter
import handlers

from loader import bot
from utils.set_bot_commands import set_default_commands
from database.models import create_models

"""
Основной файл для запуска бота.

Импорты:
- StateFilter: Пользовательский фильтр для фильтрации сообщений по состояниям.
- handlers: Модуль с обработчиками сообщений.
- bot: Экземпляр бота, созданный с использованием TeleBot и StateMemoryStorage.
- set_default_commands: Функция для установки стандартных команд бота.
- create_models: Функция для создания таблиц в базе данных.

"""

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    create_models()
    set_default_commands(bot)
    bot.infinity_polling()
