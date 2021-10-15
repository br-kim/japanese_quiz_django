from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.template.backends.jinja2 import Jinja2

from . import views

urlpatterns = [
    path('create_user_page', views.create_user_page),
    path('login', auth_views.LoginView.as_view(template_name='login.html',
                                               template_engine='jinja2'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]