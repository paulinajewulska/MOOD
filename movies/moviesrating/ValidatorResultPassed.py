from movies.moviesrating.ValidatorResult import ValidatorResult


class ValidatorResultPassed (ValidatorResult):
    def is_valid(self):
        return True
