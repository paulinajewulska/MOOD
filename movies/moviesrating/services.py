from mood.settings import BASE_DIR

from movies.moviesrating.MovieStorageService import MovieStorageService
from movies.moviesrating.MovieRepositoryImdbJson import MovieRepositoryImdbJson

from movies.moviesrating.MovieRatingService import MovieRatingService
from movies.moviesrating.MovieRatingRepositoryMemoryStorage import MovieRatingRepositoryMemoryStorage


def _init_movie_storage_service():
    print("Create movie storage service...")
    repository = MovieRepositoryImdbJson(BASE_DIR+'\\templates\\MovieDatabase.json')
    return MovieStorageService(repository)


def _init_movie_rating_service():
    print("Create movie rating service...")
    return MovieRatingService(MovieRatingRepositoryMemoryStorage())


MOVIE_STORAGE_SERVICE = _init_movie_storage_service()
MOVIE_RATING_SERVICE = _init_movie_rating_service()