from django.conf.urls import include
from django.urls import path
from community import views


urlpatterns = [
    path('', views.main),
    path('write_page', views.write_page),
    path('write', views.write),
    path('edit_page', views.edit_page),
    path('edit/<int:article_id>', views.edit),
    path('delete/<int:article_id>', views.delete),
    path('article/<int:article_id>', views.get_article),
    path('article_page/<int:page_num>', views.get_article_page),
]