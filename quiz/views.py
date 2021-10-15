import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

import quiz.util
from . import service


def inf_quiz(request):
    return render(request, "quiz.html")


def lim_quiz(request):
    return render(request, "new_quiz.html")


def quiz_img(request):
    kind = request.GET.get("kind")
    return JsonResponse({"path": quiz.util.get_gana_url(kind)})


def quiz_imgs(request):
    kind = request.GET.get("kind")
    return JsonResponse({"order": quiz.util.get_gana_url_list(kind)})


def score_update(request):
    body = json.loads(request.body)
    kind = body.get("kind")
    character = body.get("character")
    service.update_score(kind, character, request.user)
    return HttpResponse(status=204)
