import requests
import json
from cogs.movies.movie import Movie
from cogs.movies.series import Series
from cogs.movies.detailed_movie import DetailedMovie
from cogs.movies.detailed_series import DetailedSeries
from random import choice, randint


class ShowsService:

    def __init__(self, authorization_token):
        self.authorization_token = authorization_token

    def _get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )
        return response

    # region Movies
    def get_popular_movies(self):
        url = f"https://api.themoviedb.org/3/movie/popular?language=pt&page={randint(1, 500)}"
        response = self._get_api_request(url)
        response_json = response.json()
        movies_json = json.loads(json.dumps(response_json).replace("False", "false").replace("True", "true"))
        try:
            movies = [Movie(**show_json) for
                      show_json in movies_json["results"]]
            return movies
        except NameError:
            print(response_json)
            return None

    def get_one_popular_movie_detailed(self):
        show_id = choice(self.get_popular_movies()).id
        return self.get_movie_detailed(show_id)

    def get_movie_detailed(self, show_id):
        url = f"https://api.themoviedb.org/3/movie/{show_id}?language=pt"
        response = self._get_api_request(url)
        response_json = json.loads(json.dumps(response.json()).replace("False", "false").replace("True", "true"))
        return DetailedMovie(**response_json)

    # endregion

    # region Series
    def get_popular_show(self):
        url = f"https://api.themoviedb.org/3/tv/popular?language=pt&page={randint(1, 500)}"
        response = self._get_api_request(url)
        response_json = response.json()
        series_json = json.loads(json.dumps(response_json).replace("False", "false").replace("True", "true"))
        try:
            shows = [Series(**show_json) for
                     show_json in series_json["results"]]
            return shows
        except NameError:
            print(response_json)
            return None

    def get_one_popular_show_detailed(self):
        show_id = choice(self.get_popular_show()).id
        return self.get_show_detailed(show_id)

    def get_show_detailed(self, show_id):
        url = f"https://api.themoviedb.org/3/tv/{show_id}?language=pt"
        response = self._get_api_request(url)
        response_json = json.loads(json.dumps(response.json()).replace("False", "false").replace("True", "true"))
        return DetailedSeries(**response_json)

    # endregion
