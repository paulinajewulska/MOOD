import json

from analisys.word2vect import tokenizer_obj, max_length, model
from analisys.csvtojson import csvtojson

from tensorflow.python.keras.preprocessing.sequence import pad_sequences


def main():
    #csvtojson()

    genres = []
    with open('analisys/tmdb_movie.json') as infile:
        movie = json.load(infile)
    text = []
    movie2 = []
    g = 0
    with open('moviesent.json', 'w') as f:

        for i in range(0, len(movie)):
            if movie[i]['overview'] is not None:
                sentiment = []
                text = movie[i]['overview']
                text_tokens = tokenizer_obj.texts_to_sequences(text)
                tex_tokens_pad = pad_sequences(text_tokens, maxlen=max_length)
                sentiment = model.predict(x=tex_tokens_pad)
                movie2.append({"title": movie[i]['original_title'], "year": movie[i]['release_year'],
                               "director": movie[i]['director'], "cast": movie[i]['cast'], "link": movie[i]['homepage'],
                               "ratings": movie[i]['vote_average'], "genres": movie[i]['genres'],
                               "duration": movie[i]['runtime'], "overview": movie[i]['overview'],
                               "sentiment": float(str(sentiment[0][0]))})

        # print(sentiment)
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
