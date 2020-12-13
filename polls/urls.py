from django.urls import path

from . import views

urlpath = [
    path('', views.index, name='index'),
]