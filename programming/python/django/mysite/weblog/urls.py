from django.urls import path, include

from . import views

app_name = 'weblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('weblog_test/', views.weblog_test, name='weblog_test'),
    path('author/', views.author, name='author'),
    path('author_test/', views.author_test, name='author_test'),
    path('author_delete/', views.author_delete, name='author_delete'),
    path('author_add/', views.author_add, name='author_add'),
    path('add_author/', views.add_author, name='add_author'),
]