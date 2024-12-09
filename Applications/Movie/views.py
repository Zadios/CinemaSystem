from django.views.generic import ListView
from django.shortcuts import render
from .models import Film
from Applications.Showtime.models import Movie_Theater


def pelicula_list(request):
    films = Film.objects.all()
    return render(request, 'movie/index.html', {'films': films})

def proximos_estrenos(request):
    films = Film.objects.all()
    return render(request, 'movie/estrenos.html', {'films': films})