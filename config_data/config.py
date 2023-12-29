import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

vars_list = ['BOT_TOKEN', 'API_KEY', 'BASE_URL']

ENVS = dict()
for element in vars_list:
    value = os.getenv(element)
    if value:
        ENVS[element] = value
    else:
        exit('{} отсутствует в переменных окружения'.format(element))

DB_PATH = os.path.join('database', 'database.db')

DEFAULT_COMMANDS = (
    ('start', 'Запустить бота.'),
    ('help', 'Получить информацию о командах')
)
