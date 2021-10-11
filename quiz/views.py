from django.shortcuts import render
from django.http.response import HttpResponse

from .models import User


def hello(request):
    user_list = User.objects.order_by('user_id')
    return HttpResponse(user_list)


def user_register(request):
    print(request.GET)
    return HttpResponse(request.body)
