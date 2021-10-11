from django.conf.urls import include
from django.urls import path
from quiz import views


urlpatterns = [
    path('inf_quiz', views.inf_quiz),
    path('lim_quiz', views.lim_quiz),
    path('scoreboard', None),
]