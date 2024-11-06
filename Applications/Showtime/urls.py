from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "showtime"
urlpatterns = [
    path('<int:film_id>/', views.comprar_entradas, name='comprar_entradas'),
]