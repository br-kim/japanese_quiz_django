from django.conf.urls import include
from django.urls import path
from quiz import views


urlpatterns = [
    path('inf_quiz', views.inf_quiz),
    path('lim_quiz', views.lim_quiz),
    path('quiz_img', views.quiz_img),
    path('quiz_imgs', views.quiz_imgs),
    path('score_update', views.score_update),
]