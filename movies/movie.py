from typing import List
from datetime import datetime


class Movie:
    adult: bool
    backdrop_path: str
    id: int
    title: str
    original_language: str
    original_title: str
    overview: str
    poster_path: str
    media_type: str
    genre_ids: List[int]
    popularity: float
    release_date: datetime
    video: bool
    vote_average: float
    vote_count: int

    def __init__(self, adult: bool, backdrop_path: str, id: int, title: str, original_language: str,
                 original_title: str, overview: str, poster_path: str, genre_ids: List[int],
                 popularity: float, release_date: datetime, video: bool, vote_average: float, vote_count: int,
                 media_type: str = None) -> None:
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.id = id
        self.title = title
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.poster_path = poster_path
        self.media_type = media_type
        self.genre_ids = genre_ids
        self.popularity = popularity
        self.release_date = release_date
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count
