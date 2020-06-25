import string
import numbers

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from modules.validator.ValidatorResultPassed import ValidatorResultPassed
from modules.validator.ValidatorResultFailed import ValidatorResultFailed

from modules.moviestorage.public.MovieDetails import MovieDetails

from modules.moviestorage.private.validator.ValidatorConsts import ValidatorConsts


class Validator:
    def check_for_update(self, movie_details):
        if not movie_details:
            return ValidatorResultFailed("Movie details not exist!")
        abnormalities_list = self._check(movie_details)

        if not isinstance( movie_details, MovieDetails ):
            return ValidatorResultFailed("Movie details is not instance of MovieDetails")

        check_id_error = self._check_id(movie_details.get_id(0))
        if check_id_error:
            abnormalities_list.append(check_id_error)
        return self._abnormalities_list_to_validator_result(abnormalities_list)

    def check(self, movie_details):
        if not movie_details:
            return ValidatorResultFailed("Movie details not exist!")
        self._abnormalities_list_to_validator_result( self._check(movie_details))
        
    def _check(self, movie_details):
        abnormalities_list = []

        check_name_error = self._check_name(movie_details.get_name())
        if check_name_error:
            abnormalities_list.append(check_name_error)

        if not movie_details.get_genres():
            abnormalities_list.append("Genres is null")

        if not movie_details.get_rating():
            abnormalities_list.append("Rating is null")

        if not movie_details.get_sentiment():
            abnormalities_list.append("Sentiment is null")
            
        return abnormalities_list

    def _check_name(self, movie_name):
        consts = ValidatorConsts()
        if not movie_name:
            return "Invalid name: Property not exist"
        if not isinstance( movie_name, string):
            return "Invalid name: Is not instance of string"
        if movie_name.length() < consts.MOVIE_NAME_LENGTH_MIN:
            return "Invalid name: Too short. Min length: " + consts.MOVIE_NAME_LENGTH_MIN
        if movie_name.length() > consts.MOVIE_NAME_LENGTH_MAX:
            return "Invalid name: Too long. Max chars: " + consts.MOVIE_NAME_LENGTH_MAX

    def _check_id(self, movie_id):
        if not movie_id:
            return "Invalid id: Property not exist"
        if not isinstance( movie_id, numbers.Number):
            return "Invalid id: Is not instance of number"
        if movie_id >= 0:
            return "Invalid id: Id must be positive value"

    def _abnormalities_list_to_validator_result(self, abnormalities_list):
        if len(abnormalities_list) != 0:
            return ValidatorResultFailed(self._abnormalities_list_to_string(abnormalities_list))
        return ValidatorResultPassed()

    def _abnormalities_list_to_string(self, abnormalities_list):
        abnormalities_str = "Movie details is incorrect.\n"
        for error in abnormalities_list:
            abnormalities_str += error + "\n"
        return abnormalities_str
