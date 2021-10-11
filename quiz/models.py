from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=20)
