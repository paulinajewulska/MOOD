from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    question_category = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    coefficient = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.choice_text
