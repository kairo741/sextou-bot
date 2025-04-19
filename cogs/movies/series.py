from datetime import datetime
from typing import List


class Series:
    backdrop_path: str
    first_air_date: datetime
    genre_ids: List[int]
    id: int
    name: str
    origin_country: List[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str
    vote_average: float
    vote_count: int

    def __init__(self, adult: bool, backdrop_path: str, first_air_date: datetime, genre_ids: List[int], id: int,
                 name: str, origin_country: List[str], original_language: str, original_name: str, overview: str,
                 popularity: float, poster_path: str, vote_average: float, vote_count: int) -> None:
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.first_air_date = first_air_date
        self.genre_ids = genre_ids
        self.id = id
        self.name = name
        self.origin_country = origin_country
        self.original_language = original_language
        self.original_name = original_name
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.vote_average = vote_average
        self.vote_count = vote_count
