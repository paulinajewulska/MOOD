import json
from analisys.analyzer import analyzer


def filtermovie(genre, answer1, answer2, answer3, answer4, answer5):
    sentanswer1 = analyzer(answer1)
    sentanswer2 = analyzer(answer2)
    sentanswer3 = analyzer(answer3)
    sentanswer4 = analyzer(answer4)
    sentanswer5 = analyzer(answer5)
    sentgenre = analyzer(genre)
    sentuser = (sentanswer1 + sentanswer2 +
                sentanswer3 + sentanswer4 + sentanswer5 + sentgenre) / 5
    movie2 = []
    with open('movies/moviesent.json') as infile:
        movie = json.load(infile)

    for i in range(0, len(movie)):
        txt = movie[i]['genres']
        x = txt.split("|")
        for y in range(0, len(x)):
            if genre.lower() in x[y].lower():
                if movie[i]['sentiment'] >= sentuser:
                    movie2.append(
                        {"title": movie[i]['title'], "ratings": movie[i]['ratings'], "genres": movie[i]['genres']})
    return (movie2)
