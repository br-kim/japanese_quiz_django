from django.core.paginator import Paginator

from community import models


def create_article(writer, title, contents):
    article = models.Articles.objects.create(user_id=writer, title=title, contents=contents)
    return article.save()


def create_comment(writer, contents, article_id, parent_id):
    comment = models.Comments.objects.create(
        user_id=writer, contents=contents, article_id=article_id, parent_id=parent_id)
    return comment.save()


def get_article_list(page_num):
    p = Paginator(models.Articles.objects.order_by("id").all(), 3)
    return p.page(page_num).object_list


def get_articles_size():
    return models.Articles.objects.order_by("id").all().count()


def get_article(article_id):
    return models.Articles.objects.get(id=article_id)


def delete_article(article_id):
    return models.Articles.objects.filter(id=article_id).delete()


def edit_article(article_id, title, contents):
    article = models.Articles.objects.get(id=article_id)
    if title:
        article.title = title
    if contents:
        article.contents = contents
    return article.save()


def get_comments(article_id):
    return models.Comments.objects.filter(article_id=article_id)


def delete_comment(comment_id):
    return models.Comments.objects.filter(id=comment_id).delete()


def edit_comment(comment_id, contents):
    comment = models.Comments.objects.get(id=comment_id)
    comment.contents = contents
    return comment.save()
