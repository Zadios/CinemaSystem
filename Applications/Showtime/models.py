from django.db import models
from Applications.Movie.models import Format

# Create your models here.

class Movie_Theater(models.Model):
    id_movie_theater = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    capacity = models.IntegerField('Capacidad', null=True)
    formats = models.ManyToManyField(Format)
