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
DATE_FORMAT = "%d.%m.%Y"

DEFAULT_COMMANDS = (
    ('start', 'Запустить бота. ▶️'),
    ('help', 'Получить информацию о командах. 🆘'),
    ('high', 'Подборки фильмов с самыми высокими рейтингами сайтов Кинопоиск или IMDb или самые длинные фильмы! ⬆️'),
    ('low', 'Подборки фильмов с самым низким возрастным рейтингом, самые старые или самые короткие фильмы! ⬇️'),
    ('custom', 'Подборки фильмов по заданным параметрам. *️⃣'),
    ('history', 'История запросов. 📝'),
    ('cancel', 'Завершение работы с ботом. 🔚')
)
