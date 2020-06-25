from django.shortcuts import render, redirect

from modules.movierating.public.MovieRating import MovieRating
from modules.movierating.public.MovieWithRating import MovieWithRating
from mood.services import MOVIE_STORAGE_SERVICE, MOVIE_RATING_SERVICE


def choice_movie(request):
    if request.method == 'POST':
        user_id = request.user.id
        if not user_id:
            raise Exception('User id is null')

        movie_id = request.POST['movie_id']
        if not movie_id:
            raise Exception('Movie id is null')

        MOVIE_RATING_SERVICE.add_movie_to_rating(user_id, int(movie_id))
        return redirect('movies_rating')
    raise Exception('Bad http method')

def get_movies_rating(request):
    if request.method == 'GET':
        user_id = request.user.id
        if not user_id:
            raise Exception('User id is null')
        return render(request, 'rated_movie.html', {'rated_movie': _get_rated_movie_collection(int(user_id))})

    if request.method == 'POST':
        user_id = request.user.id
        if not user_id:
            raise Exception('User id is null')
        movie_id = request.POST['movie_id']
        if not movie_id:
            raise Exception('Movie id is null')
        rating = request.POST['rating']
        if not rating:
            raise Exception('Rating is null')

        MOVIE_RATING_SERVICE.rated_by_user(MovieWithRating(int(user_id), int(movie_id), MovieRating(int(rating))))
        return render(request, 'rated_movie.html', {'rated_movie': _get_rated_movie_collection(int(user_id))})
    raise Exception("Bad http method")


def _get_rated_movie_collection( user_id ):
    movie_rating_collection = MOVIE_RATING_SERVICE.get_all_of_user(user_id)
    rated_movies = []

    for rated_movie in movie_rating_collection:
        rated_movies.append({
            'rating': rated_movie.get_rating(),
            'movie_details': MOVIE_STORAGE_SERVICE.get_by_id(rated_movie.get_movie_id())
        })

    return rated_movies
