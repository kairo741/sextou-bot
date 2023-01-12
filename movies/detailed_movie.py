from typing import List
from datetime import datetime


class Genre:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class ProductionCompany:
    id: int
    logo_path: None
    name: str
    origin_country: str

    def __init__(self, id: int, logo_path: None, name: str, origin_country: str) -> None:
        self.id = id
        self.logo_path = logo_path
        self.name = name
        self.origin_country = origin_country


class ProductionCountry:
    iso_3166_1: str
    name: str

    def __init__(self, iso_3166_1: str, name: str) -> None:
        self.iso_3166_1 = iso_3166_1
        self.name = name


class SpokenLanguage:
    english_name: str
    iso_639_1: str
    name: str

    def __init__(self, english_name: str, iso_639_1: str, name: str) -> None:
        self.english_name = english_name
        self.iso_639_1 = iso_639_1
        self.name = name


class DetailedMovie:
    adult: bool
    backdrop_path: str
    belongs_to_collection: None
    budget: int
    genres: List[Genre]
    homepage: str
    id: int
    imdb_id: str
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: List[ProductionCompany]
    production_countries: List[ProductionCountry]
    release_date: datetime
    revenue: int
    runtime: int
    spoken_languages: List[SpokenLanguage]
    status: str
    tagline: str
    title: str
    video: bool
    vote_average: float
    vote_count: int

    def __init__(self, adult: bool, backdrop_path: str, belongs_to_collection: None, budget: int, genres: List[Genre],
                 homepage: str, id: int, imdb_id: str, original_language: str, original_title: str, overview: str,
                 popularity: float, poster_path: str, production_companies: List[ProductionCompany],
                 production_countries: List[ProductionCountry], release_date: datetime, revenue: int, runtime: int,
                 spoken_languages: List[SpokenLanguage], status: str, tagline: str, title: str, video: bool,
                 vote_average: float, vote_count: int) -> None:
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.belongs_to_collection = belongs_to_collection
        self.budget = budget
        self.genres = genres
        self.homepage = homepage
        self.id = id
        self.imdb_id = imdb_id
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.release_date = release_date
        self.revenue = revenue
        self.runtime = runtime
        self.spoken_languages = spoken_languages
        self.status = status
        self.tagline = tagline
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count
