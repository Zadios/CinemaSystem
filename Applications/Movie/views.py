from django.views.generic import ListView
from django.shortcuts import render
from .models import Pelicula

def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'movie/pelicula_list.html', {'peliculas': peliculas})

