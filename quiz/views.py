import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

import quiz.util
from . import service

ERROR_PAGE = "/user/need_login"


@login_required(login_url=ERROR_PAGE)
def inf_quiz(request):
    return render(request, "quiz.html")


@login_required(login_url=ERROR_PAGE)
def lim_quiz(request):
    return render(request, "new_quiz.html")


@login_required(login_url=ERROR_PAGE)
def quiz_img(request):
    kind = request.GET.get("kind")
    return JsonResponse({"path": quiz.util.get_gana_url(kind)})


@login_required(login_url=ERROR_PAGE)
def quiz_imgs(request):
    kind = request.GET.get("kind")
    return JsonResponse({"order": quiz.util.get_gana_url_list(kind)})


@login_required(login_url=ERROR_PAGE)
def score_update(request):
    body = json.loads(request.body)
    kind = body.get("kind")
    character = body.get("character")
    service.update_score(kind, character, request.user)
    return HttpResponse(status=204)
