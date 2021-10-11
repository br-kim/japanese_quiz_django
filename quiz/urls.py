from django.conf.urls import include
from django.urls import path
from quiz import views


urlpatterns = [
    path('hello', views.hello),
    path('user_register', views.user_register)
]