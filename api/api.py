import requests
from typing import Dict, Any

from config_data.config import ENVS


def api_request(sort_type: int) -> requests.Response:
    headers: Dict[str, str] = {
        'accept': 'application/json',
        'X-API-KEY': ENVS.get('API_KEY')
    }
    params: Dict[str, Any] = {
        'page': 1,
        'limit': 10,
        'sortField': 'rating.kp',
        'sortType': sort_type,
        'selectFields': ['name', 'enName', 'description', 'status', 'rating', 'ageRating'],
        'notNullFields': ['name', 'enName']
    }
    response = requests.get('{}/movie'.format(ENVS.get('BASE_URL')), params=params, headers=headers)
    return response


def movie_rating(sort_type: int):
    movie_response = api_request(sort_type=sort_type)
    if movie_response.status_code != 200:
        print('Не удалось получить список фильмов')
        exit(1)

    movie_data = movie_response.json()
    return movie_data
