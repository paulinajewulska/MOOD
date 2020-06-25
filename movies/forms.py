from django import forms
import json
import random
import pandas as pd


def sort_movies():
    with open("movies/basic_movies.json") as f:
        file_movies = json.load(f)
    movies = []
    for movie in file_movies:
        movies.append(movie['fields'])
    movies.sort(key=lambda x: x.get('ratings'), reverse=True)
    return movies


def sort2_movies():
    with open("movies\moviesent.json") as f:
        file_movies = json.load(f)
    movies = []
    for movie in file_movies:
        movie['mood_rate'] = 0
        movie['votes_number'] = 0
        movies.append(movie)
    movies.sort(key=lambda x: x.get('ratings'), reverse=True)
    return movies


class GetRatingMovies(forms.Form):
    options = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating = forms.ChoiceField(choices=options)
