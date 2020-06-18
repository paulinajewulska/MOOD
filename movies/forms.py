from django import forms
import json
import random

def sort_movies():
    with open('movies/basic_movies.json') as f:
        file_movies = json.load(f)
    movies = []
    for movie in file_movies:
        movies.append(movie['fields'])
    movies.sort(key=lambda x: x.get('ratings'), reverse=True)
    return movies

class GetRatingMovies(forms.Form):
    options = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = forms.ChoiceField(choices=options)
