from django.shortcuts import render
from .models import Movie
from movies.forms import sort_movies, GetRatingMovies
from decimal import Decimal
from mood.services import MOVIE_STORAGE_SERVICE


def get_movie_list(request):
    all_movies = Movie.objects.all()
    context = {
        "movies": all_movies,
    }

    return render(request, "movies_list.html", context)


def sort_movie_list(request):
    all_movies = sort_movies()
    form = GetRatingMovies()
    context = {
        "movies": all_movies,
        'form': form,
    }
    if request.method == 'POST':
        form = GetRatingMovies(request.POST)
        result = {
            'rating': request.POST['rating'],
            'title': request.POST['title'],
        }

        # for movie in all_movies:
        #   if movie['title'] == result['title']:
        #      movie['votes_number'] += 1
        #     new_mood_rate = (movie['mood_rate'] + Decimal(result["rating"])) / movie['votes_number']
        #    movie['mood_rate'] = new_mood_rate

        chosen_movie = Movie.objects.filter(title=result["title"])[0]
        chosen_movie.votes_number = 1
        new_mood_rate = (chosen_movie.mood_rate +
                         Decimal(result["rating"])) / chosen_movie.votes_number
        chosen_movie.mood_rate += new_mood_rate
        chosen_movie.save()

        context = {
            "movies": all_movies,
            'form': form,
        }
    return render(request, "movies_list.html", context)


def get_movies_sorted_by_mood_rating(request):
    all_movies = list(Movie.objects.all())
    all_movies.sort(key=lambda x: x.mood_rate, reverse=True)
    form = GetRatingMovies()

    context = {
        "movies": all_movies,
        'form': form,
    }
    return render(request, "movies_list.html", context)


def get_movies_list_sort_by_rating(request):
    all_movies = list(Movie.objects.all())
    all_movies.sort(key=lambda x: x.ratings, reverse=True)
    form = GetRatingMovies()

    context = {
        "movies": all_movies,
        'form': form,
    }
    return render(request, "movies_list.html", context)
