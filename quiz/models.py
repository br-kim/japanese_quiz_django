from django.db import models


class Score(models.Model):
    user_id = models.CharField(max_length=20)
    hiragana_score = models.JSONField(default=dict)
    katakana_score = models.JSONField(default=dict)
