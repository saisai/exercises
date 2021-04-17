from django.urls import path, include

from . import views

app_name = 'weblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('weblog_test/', views.weblog_test, name='weblog_test'),
]