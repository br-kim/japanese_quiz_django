from django.conf.urls import include
from django.urls import path
from community import views


urlpatterns = [
    path('', views.main),
    path('', views.write),
]