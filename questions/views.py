from typing import Dict, Any

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from movies.filtermovie import filtermovie
from .forms import GetMoviePreferences
from mood.services import MOVIE_STORAGE_SERVICE, MOVIE_RATING_SERVICE


def get_all_questions(request):

    form = GetMoviePreferences()
    context = {
        'form': form,
    }

    return render(request, 'questions.html', context)

votes = [0,0,0,0,0,0,0,0,0,0,0,0]
votes2 = [0,0,0,0,0]
def get_results(request):

    if request.method == 'POST':

        form = GetMoviePreferences(request.POST)
        result = {
            'mood': request.POST['mood'],
            'genre': request.POST['genre'],
            'will_lead_to_reflect': request.POST['will_lead_to_reflect'],
            'lead_to_think': request.POST['lead_to_think'],
            'kind': request.POST['kind'],
            "loud_movies": request.POST["loud_movies"]

        }
        Category = ['horror', 'comedy', 'action', 'crime', 'fantasy', 'history', 'adventure',
                    'romance', 'science fiction', 'thriller', 'western', 'animation']
        vote = request.POST['genre']

        for choose in Category:
            if choose == vote:
                votes[Category.index(choose)] += 1

        stat = pd.DataFrame({'Category': Category, 'Label':votes})
        stat.to_csv(os.getcwd() + '/statistic.csv', index=False)

        Mood = ["I'm happy", "I am okey", "I'm so bored", "I'm sad", "I hate the world"]
        vote2 = request.POST['mood']

        for choose in Mood:
            if choose == vote2:
                votes2[Mood.index(choose)] += 1

        stat2 = pd.DataFrame({'Mood': Mood, 'Label':votes2})
        stat2.to_csv(os.getcwd() + '/statistic2.csv', index=False)


        movies = filtermovie(
            result['genre'], result['mood'], result['will_lead_to_reflect'], result['lead_to_think'], result['kind'], result['loud_movies'])

        context = {
            'movies': movies
        }
        return render(request, 'results.html', context)


