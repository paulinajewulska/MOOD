"""mood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from movie_rating.views import get_movies_rating, choice_movie
from questions.views import get_all_questions, get_results
from movies.views import sort_movie_list, get_movies_sorted_by_mood_rating, get_movies_list_sort_by_rating

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # new
    path("users/", include("django.contrib.auth.urls")),
    path("questions/", get_all_questions, name="questions"),
    path("results/", get_results, name="results"),
    path("results/choice", choice_movie, name="choice_movie"),
    path("movies_list/", sort_movie_list, name="movies_list"),
    path("movies_rating/", get_movies_rating, name="movies_rating"),
    path("movies_list_sort_by_mood_rating/", get_movies_sorted_by_mood_rating, name="movies_list_sort_by_mood_rating"),
    path("movies_list_sort_by_rating/", get_movies_list_sort_by_rating, name="movies_list_sort_by_rating"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
