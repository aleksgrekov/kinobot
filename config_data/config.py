import os
from dotenv import load_dotenv, find_dotenv
from typing import List

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

vars_list: List[str] = ['BOT_TOKEN', 'API_KEY', 'BASE_URL']

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
    ('help', 'Получить информацию о командах'),
    ('high', 'Подборка фильмов с самым высоким рейтингом!'),
    ('cancel', 'Завершение работы с ботом!'),
)
