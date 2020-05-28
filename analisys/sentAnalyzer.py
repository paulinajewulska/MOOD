import json
from analisys.analyzer import analyzer
from scripts.downloadfile import downloadfile
from analisys.csvtojson import csvtojson

def main():
    downloadfile()
    csvtojson()
    movie2 = []
    genres = []
    with open('movie.json') as infile:
        movie = json.load(infile)

    with open('moviesent.json', 'w') as f:
        for i in range(0, len(movie)):
            if movie[i]['overview'] is not None:
                movie2.append({"title": movie[i]['original_title'],"year": movie[i]['release_year'],
                               "director": movie[i]['director'],"cast": movie[i]['cast'],"link": movie[i]['homepage'],
                               "ratings": movie[i]['vote_average'],"genres":movie[i]['genres'],"duration":movie[i]['runtime'],"overview":movie[i]['overview'],
                               "sentiment": analyzer(movie[i]['overview'])})
        json.dump(movie2, f, indent=2)

    with open('genres.json', 'w') as f1:
        for i in range(0, len(movie)):
            txt = movie[i]['genres']
            if txt is not None:
                x = txt.split("|")
                for y in range(0, len(x)):
                    if x[y] not in genres:
                        genres.append(x[y])
        json.dump(genres, f1, indent=2)


if __name__ == "__main__":
    main()
