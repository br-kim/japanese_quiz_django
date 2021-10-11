from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=20)


class Score(models.Model):
    user_id = models.CharField(max_length=20)
    hiragana_score = models.CharField(max_length=20)
    katakana_score = models.CharField(max_length=20)
