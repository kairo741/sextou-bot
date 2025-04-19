from datetime import datetime
from typing import Optional, List, Any


class CreatedBy:
    id: int
    credit_id: str
    name: str
    gender: int
    profile_path: str

    def __init__(self, id: int, credit_id: str, name: str, gender: int, profile_path: str) -> None:
        self.id = id
        self.credit_id = credit_id
        self.name = name
        self.gender = gender
        self.profile_path = profile_path


class Genre:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class LastEpisodeToAir:
    air_date: datetime
    episode_number: int
    id: int
    name: str
    overview: str
    production_code: str
    runtime: int
    season_number: int
    show_id: int
    still_path: str
    vote_average: float
    vote_count: int

    def __init__(self, air_date: datetime, episode_number: int, id: int, name: str, overview: str, production_code: str,
                 runtime: int, season_number: int, show_id: int, still_path: str, vote_average: float,
                 vote_count: int) -> None:
        self.air_date = air_date
        self.episode_number = episode_number
        self.id = id
        self.name = name
        self.overview = overview
        self.production_code = production_code
        self.runtime = runtime
        self.season_number = season_number
        self.show_id = show_id
        self.still_path = still_path
        self.vote_average = vote_average
        self.vote_count = vote_count


class Network:
    id: int
    name: str
    logo_path: Optional[str]
    origin_country: str

    def __init__(self, id: int, name: str, logo_path: Optional[str], origin_country: str) -> None:
        self.id = id
        self.name = name
        self.logo_path = logo_path
        self.origin_country = origin_country


class ProductionCountry:
    iso_3166_1: str
    name: str

    def __init__(self, iso_3166_1: str, name: str) -> None:
        self.iso_3166_1 = iso_3166_1
        self.name = name


class Season:
    air_date: Optional[datetime]
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: Optional[str]
    season_number: int

    def __init__(self, air_date: Optional[datetime], episode_count: int, id: int, name: str, overview: str,
                 poster_path: Optional[str], season_number: int) -> None:
        self.air_date = air_date
        self.episode_count = episode_count
        self.id = id
        self.name = name
        self.overview = overview
        self.poster_path = poster_path
        self.season_number = season_number


class SpokenLanguage:
    english_name: str
    iso_639_1: str
    name: str

    def __init__(self, english_name: str, iso_639_1: str, name: str) -> None:
        self.english_name = english_name
        self.iso_639_1 = iso_639_1
        self.name = name


class DetailedSeries:
    adult: bool
    backdrop_path: str
    created_by: List[CreatedBy]
    episode_run_time: List[Any]
    first_air_date: datetime
    genres: List[Genre]
    homepage: str
    id: int
    in_production: bool
    languages: List[str]
    last_air_date: datetime
    last_episode_to_air: LastEpisodeToAir
    name: str
    next_episode_to_air: None
    networks: List[Network]
    number_of_episodes: int
    number_of_seasons: int
    origin_country: List[str]
    original_language: str
    original_name: str
    overview: str
    popularity: float
    poster_path: str
    production_companies: List[Network]
    production_countries: List[ProductionCountry]
    seasons: List[Season]
    spoken_languages: List[SpokenLanguage]
    status: str
    tagline: str
    type: str
    vote_average: float
    vote_count: int

    def __init__(self, adult: bool, backdrop_path: str, created_by: List[CreatedBy], episode_run_time: List[Any],
                 first_air_date: datetime, genres: List[Genre], homepage: str, id: int, in_production: bool,
                 languages: List[str], last_air_date: datetime, last_episode_to_air: LastEpisodeToAir, name: str,
                 next_episode_to_air: None, networks: List[Network], number_of_episodes: int, number_of_seasons: int,
                 origin_country: List[str], original_language: str, original_name: str, overview: str,
                 popularity: float, poster_path: str, production_companies: List[Network],
                 production_countries: List[ProductionCountry], seasons: List[Season],
                 spoken_languages: List[SpokenLanguage], status: str, tagline: str, type: str, vote_average: float,
                 vote_count: int) -> None:
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.created_by = created_by
        self.episode_run_time = episode_run_time
        self.first_air_date = first_air_date
        self.genres = genres
        self.homepage = homepage
        self.id = id
        self.in_production = in_production
        self.languages = languages
        self.last_air_date = last_air_date
        self.last_episode_to_air = last_episode_to_air
        self.name = name
        self.next_episode_to_air = next_episode_to_air
        self.networks = networks
        self.number_of_episodes = number_of_episodes
        self.number_of_seasons = number_of_seasons
        self.origin_country = origin_country
        self.original_language = original_language
        self.original_name = original_name
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.seasons = seasons
        self.spoken_languages = spoken_languages
        self.status = status
        self.tagline = tagline
        self.type = type
        self.vote_average = vote_average
        self.vote_count = vote_count
