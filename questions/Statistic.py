from django.shortcuts import render
from django.views import generic
from movies.filtermovie import filtermovie
from .forms import GetMoviePreferences
import pandas as pd
import numpy as np
import matplotlib as plt
Category = ['horror', 'comedy', 'action','crime', 'fantasy', 'history','adventure',
            'romance','science fiction','thriller','western','animation']
def statistic_positive(request):
    votes = []
    if request.method == 'POST':
        form = GetMoviePreferences(request.POST)
        vote = request.POST['genre']
        if vote == 'horror':
            votes[0] =+1
        if vote == 'comedy':
            votes[1] =+1
        if vote == 'action':
            votes[2] =+1
        if vote == 'crime':
            votes[3] =+1
        if vote == 'fantasy':
            votes[4] =+1
        if vote == 'history':
            votes[5] =+1
        if vote == 'adventure':
            votes[6] =+1
        if vote == 'romance':
            votes[7] =+1
        if vote == 'science fiction':
            votes[8] =+1
        if vote == 'thriller':
            votes[9] =+1
        if vote == 'western':
            votes[10] =+1
        if vote == 'animation':
            votes[11] = +1
    return votes

def char_positive():
    x_axis = Category
    y_axis = statistic_positive()
    y_pos = np.arange(len(y_axis))
    plt.figure(figsize=(10, 5))
    plt.bar(y_pos, y_axis)
    plt.xticks(y_pos, x_axis)
    plt.title('What categories we choose the most')
    plt.show()


