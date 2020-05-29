from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, default=' ')
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    genres = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    mood_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    votes_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title