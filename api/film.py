class Film:
    def __init__(self, rating, movielength, name, description, year, poster, genres, countries, enname, agerating):
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

    def __str__(self):
        movie_data = f'Название: {self.__name}'
        if self.__enname:
            movie_data += f'\n{self.__enname}'
        genres = [genre.get('name') for genre in self.__genres]
        if genres:
            movie_data += '\n' + ', '.join(genres)
        countries = [country.get('name') for country in self.__countries]
        if countries:
            movie_data += '\n' + ', '.join(countries)
        movie_data += f"\n\nРейтинг сайта \"Кинопоиск\": {self.__rating.get('kp', 'рейтинг скрыт')}"
        if self.__year:
            movie_data += f'\nГод выпуска: {self.__year}'
        if self.__agerating:
            movie_data += f'\nВозрастной рейтинг: {self.__agerating}'
        if self.__movielength:
            movie_data += f'\nПродолжительность: {self.__movielength} мин.'
        if self.__description:
            movie_data += f'\n\nОписание:\n{self.__description}'

        return movie_data
