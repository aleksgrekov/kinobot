class Film:
    def __init__(self, rating: dict, movielength: int, name: str, description: str,
                 year: int, poster: dict, genres: list, countries: list, enname: str, agerating: int):
        """
        Конструктор класса Film.

        :param rating: Рейтинг фильма на КиноПоиске и IMDb.
        :type rating: dict

        :param movielength: Продолжительность фильма в минутах.
        :type movielength: int

        :param name: Название фильма.
        :type name: str

        :param description: Описание фильма.
        :type description: str

        :param year: Год выпуска фильма.
        :type year: int

        :param poster: Информация о постере фильма.
        :type poster: dict

        :param genres: Список жанров фильма.
        :type genres: list

        :param countries: Список стран-производителей фильма.
        :type countries: list

        :param enname: Английское название фильма.
        :type enname: str

        :param agerating: Возрастной рейтинг фильма.
        :type agerating: str

        """

        self.__name = name
        self.__enname = enname
        self.__rating = rating
        self.__description = description
        self.__year = year
        self.__agerating = agerating
        self.__movielength = movielength
        self.__genres = genres
        self.__countries = countries
        self.__poster = poster

    @property
    def poster(self):
        """
        Свойство для получения URL постера фильма.

        :return: URL постера фильма или None, если постера нет.
        :rtype: str or None

        """

        if isinstance(self.__poster, dict):
            return self.__poster.get('previewUrl', self.__poster.get('url'))
        else:
            return None

    def __str__(self):
        """
        Представление фильма в виде строки.

        :return: Строковое представление фильма.
        :rtype: str

        """

        movie_data = f'Название: {self.__name}'
        if self.__enname:
            movie_data += f'\n{self.__enname}'
        genres = [genre.get('name') for genre in self.__genres]
        if genres:
            movie_data += '\n' + ', '.join(genres)
        countries = [country.get('name') for country in self.__countries]
        if countries:
            movie_data += '\n' + ', '.join(countries)
        movie_data += '\n\nРейтинг:\n\t\tKP: {kp_rating}\n\t\tIMDb: {imdb_rating}'.format(
            kp_rating=self.__rating.get('kp', 'рейтинг скрыт'),
            imdb_rating=self.__rating.get('imdb', 'рейтинг скрыт')
        )
        if self.__year:
            movie_data += f'\nГод выпуска: {self.__year}'
        else:
            movie_data += f'\nГод выпуска не указан'
        if self.__agerating:
            movie_data += f'\nВозрастной рейтинг: {self.__agerating}'
        else:
            movie_data += f'\nБез возрастных ограничений'
        if self.__movielength:
            movie_data += f'\nПродолжительность: {self.__movielength} мин.'
        if self.__description:
            movie_data += f'\n\nОписание:\n{self.__description}'

        return movie_data
