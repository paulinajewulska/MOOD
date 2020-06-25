from enum import Enum


class MovieRating (Enum):
    VERY_GOOD = 5
    GOOD = 4
    OK = 3
    BAD = 2
    VERY_BAD = 1
    WAITING_FOR_RATING = None
