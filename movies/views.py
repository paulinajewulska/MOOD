from django.shortcuts import render
from .models import Movie
from movies.forms import RatingMovies, sort_movies
import random


def get_movie_list(request):
    all_movies = Movie.objects.all()
    context = {
        "movies": all_movies,
    }

    return render(request, "movies_list.html", context)

def sort_movie_list(request):
    all_movies = sort_movies()
    movies = RatingMovies.movie
    if request.method == 'POST':
        all_movies[3]['mood_rate'] = request.POST['rating']
    context = {
        'movies.mood_rate' : all_movies[3]['mood_rate'],
        "movies": all_movies
    }

    return render(request, "movies_list.html", context)


def movies_rating(request):
    form = RatingMovies()
    movies = RatingMovies.movie
    context = {
        'movies' : movies,
        'form': form
    }
    return render( request, 'movies_rating.html', context)


def rating(request):
    if request.method == 'POST':
        context = {'form' : request.POST}

        return render(request, "rating.html", context)
