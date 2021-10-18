from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Articles(TimestampMixin, models.Model):
    user_id = models.CharField(max_length=20)
    title = models.TextField()
    contents = models.TextField()


class Comments(TimestampMixin, models.Model):
    user_id = models.CharField(max_length=20)
    contents = models.TextField()
    article_id = models.IntegerField()
