import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота.'),
    ('hello_world', 'Тоже запускает бота.'),
    ('help', 'Получить информацию о стандартных командах')
)

# API_KEY = os.getenv("API_KEY")
