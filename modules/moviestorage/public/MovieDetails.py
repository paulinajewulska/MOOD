class MovieDetails:

    def __init__(self, id_move, name, genres, rating, sentiment):
        self._id = id_move
        self._name = name
        self._genres = genres
        self._rating = rating
        self._sentiment = sentiment

    def copy(self):
        return MovieDetails(self._id, self._name, self._genres, self._rating, self._sentiment )

    def get_id(self):
        return self._id

    def set_id(self, id_move):
        copy = self.copy()
        copy._id = id_move
        return copy

    def get_name(self):
        return self._name

    def set_name(self, name):
        copy = self.copy()
        copy._name = name
        return copy

    def get_genres(self):
        return self._genres;

    def set_genres(self, genres):
        copy = self.copy()
        copy._genres = genres
        return copy

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        copy = self.copy()
        copy._rating = rating
        return copy

    def get_sentiment(self):
        return self._sentiment

    def set_sentiment(self, sentiment):
        copy = self.copy()
        copy._sentiment = sentiment
        return copy