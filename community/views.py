from django.shortcuts import render
from django.http.response import HttpResponse

from community import service


def main(request):
    return render(request, "freeboard.html")


def write_page(request):
    return render(request, "write_article.html")


def write(request):
    return HttpResponse()


def edit_page(request):
    return render(request, "edit_article.html")


def edit(request, article_id):
    return HttpResponse()


def delete(request, article_id):
    return HttpResponse()


def get_article_page(request, page_num):
    return HttpResponse()


def get_article(request, article_id):
    return HttpResponse(article_id)
