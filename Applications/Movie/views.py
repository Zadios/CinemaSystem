from django.views.generic import ListView
from django.shortcuts import render
from .models import Film

def pelicula_list(request):
    films = Film.objects.all()
    return render(request, 'movie/pelicula_list.html', {'films': films})