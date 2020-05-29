from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    genres = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title