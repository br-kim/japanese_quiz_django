from django.shortcuts import render
from django.http.response import HttpResponse

from .models import User


def inf_quiz(request):
    return render(request, "quiz.html")


def lim_quiz(request):
    return render(request, "new_quiz.html")
