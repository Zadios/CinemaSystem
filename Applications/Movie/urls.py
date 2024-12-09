from django.contrib import admin
from django.urls import path, include
from . import views
from .views import pelicula_list, proximos_estrenos
app_name = "movie"
urlpatterns = [
    path('', pelicula_list, name='index'),
    path('estrenos/', proximos_estrenos, name='estrenos'),
]