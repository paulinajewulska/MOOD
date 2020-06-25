import json
from mood.services import MOVIE_STORAGE_SERVICE
from analisys.analyzer import analyzer


def filtermovie(genre: object, answer1: object, answer2: object, answer3: object, answer4: object, answer5: object) -> object:
    sentanswer1 = analyzer(answer1)
    sentanswer2 = analyzer(answer2)
    sentanswer3 = analyzer(answer3)
    sentanswer4 = analyzer(answer4)
    sentanswer5 = analyzer(answer5)
    sentgenre = analyzer(genre)
    sentuser = (sentanswer1 + sentanswer2 +
                sentanswer3 + sentanswer4 + sentanswer5 + sentgenre) / 5

    filtered_movies = []
    movies = MOVIE_STORAGE_SERVICE.get_all()
    for movie in movies:
        if movie.get_sentiment() < sentuser:
            continue
        if genre.lower() in movie.get_genres():
            filtered_movies.append(movie)

    return filtered_movies
