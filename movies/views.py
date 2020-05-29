from django.shortcuts import render
from .models import Movie


def get_movie_list(request):
    all_movies = Movie.objects.all()
    context = {
        "movies": all_movies,
    }

    return render(request, "movies_list.html", context)
