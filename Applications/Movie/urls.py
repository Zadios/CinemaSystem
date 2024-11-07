from django.contrib import admin
from django.urls import path, include
from . import views
from .views import pelicula_list
app_name = "movie"
urlpatterns = [
    path('', pelicula_list, name='index'),
]