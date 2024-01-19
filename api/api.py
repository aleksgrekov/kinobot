import requests
from typing import Dict, List, Any

from config_data.config import ENVS
from api.film import Film


def api_request(sort_type: int, limit: int, sort_field: str, range_value: str | None) -> requests.Response:
    """
    Выполняет запрос к API КиноПоиск для получения списка фильмов.

    :param sort_type: Тип сортировки (1 - по возрастанию, -1 - по убыванию).
    :type sort_type: int

    :param limit: Максимальное количество фильмов в ответе.
    :type limit: int

    :param sort_field: Поле для сортировки результатов запроса.
    :type sort_field: str

    :param range_value: Диапазон значений для определенного поля (год выпуска или рейтинг).
    :type range_value: str or None

    :return: Объект ответа от сервера API.
    :rtype: requests.Response

    """

    headers: Dict[str, str] = {
        'accept': 'application/json',
        'X-API-KEY': ENVS.get('API_KEY')
    }
    params: Dict[str, Any] = {
        'page': 1,
        'limit': limit,
        'sortField': sort_field,
        'sortType': sort_type,
        'type': 'movie',

        'selectFields': ['rating', 'movieLength', 'name', 'description', 'year', 'poster', 'genres', 'countries',
                         'enName', 'ageRating'],
        'notNullFields': ['name', sort_field]
    }
    if sort_field == 'year':
        if range_value:
            params[sort_field] = range_value
        else:
            params[sort_field] = '1874-2050'
    elif sort_field == 'rating.kp' and range_value:
        params[sort_field] = range_value

    response = requests.get(url=ENVS.get('BASE_URL'), params=params, headers=headers)

    return response


def suggested_films(sort_type: int, limit: int, sort_field: str, range_value: str | None) -> List[Film]:
    """
    Получает список рекомендованных фильмов на основе заданных параметров сортировки.

    :param sort_type: Тип сортировки (1 - по возрастанию, -1 - по убыванию).
    :type sort_type: int

    :param limit: Максимальное количество фильмов в ответе.
    :type limit: int

    :param sort_field: Поле для сортировки результатов запроса.
    :type sort_field: str

    :param range_value: Диапазон значений для определенного поля (год выпуска или рейтинг).
    :type range_value: str or None

    :return: Список объектов Film, представляющих рекомендованные фильмы.
    :rtype: List[Film]

    """

    movie_response: requests.Response = api_request(sort_type=sort_type, limit=limit, sort_field=sort_field,
                                                    range_value=range_value)

    if movie_response.status_code != 200:
        print('Не удалось получить список фильмов')
        exit(1)

    movie_data = movie_response.json()
    print(movie_data)

    film_list = [Film(element.get('rating'),
                      element.get('movieLength'),
                      element.get('name'),
                      element.get('description'),
                      element.get('year'),
                      element.get('poster'),
                      element.get('genres'),
                      element.get('countries'),
                      element.get('enName'),
                      element.get('ageRating'))
                 for element in movie_data['docs']]

    return film_list
