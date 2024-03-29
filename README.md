# КиноБот

КиноБот - телеграм-бот для подбора фильмов на вечер. Бот использует API сайта КиноПоиск для предоставления подборок
фильмов по различным критериям.

## Установка

1. Установите необходимые зависимости, выполнив команду:

    ```bash
    pip install -r requirements.txt
    ```

2. Создайте файл `.env` на основе `.env.template` и заполните необходимые переменные окружения.

3. Используйте команду для создания файла `.env`:

    ```bash
    dump-env --template=.env.template --prefix='YOUR_PREFIX' > .env
    ```

## Запуск

Запустите бота, выполнив команду:

```bash
python main.py
```

## Команды

- **/start:** Начать работу с ботом.
- **/help:** Получить информацию о доступных командах.
- **/high:** Подборки фильмов с самыми высокими рейтингами сайтов КиноПоиск или IMDb или самые длинные фильмы!
- **/low:** Подборки фильмов с самым низким возрастным рейтингом, самые старые или самые короткие фильмы!
- **/custom:** Подборки фильмов по заданным параметрам.
- **/history:** История запросов.
- **/cancel:** Завершение работы с ботом.

## Подборки
- "Самый высокий рейтинг КиноПоиск"
- "Самый высокий рейтинг IMDb"
- "Самые долгие фильмы"
- "Самый низкий возрастной рейтинг"
- "Самые старые фильмы"
- "Самые короткие фильмы"
- "Подборки фильмов по заданным параметрам"

## Автор
Греков Александр