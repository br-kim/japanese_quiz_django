from django.shortcuts import render
from django.http.response import HttpResponse


def main(request):
    return render(request, "freeboard.html")


def write_page(request):
    return render(request, "write_article.html")


def write(request):
    return HttpResponse()
