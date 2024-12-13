from django.views.generic import ListView
from django.shortcuts import render
from .models import Film, Banner
from Applications.Showtime.models import Movie_Theater


def pelicula_list(request):
    films = Film.objects.all()
    banners = Banner.objects.all()
    return render(request, 'movie/index.html', {'films': films, 'banners': banners})

def proximos_estrenos(request):
    films = Film.objects.all()
    return render(request, 'movie/estrenos.html', {'films': films})

def home(request):
    banners = Banner.objects.all()
    return render(request, 'movie/index.html', {'banners': banners})