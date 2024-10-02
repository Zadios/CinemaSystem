from django.contrib import admin
from models import Movie_Theater



@admin.register(Movie_Theater)
class MovieTheaterAdmin(admin.ModelAdmin):
    list_display = ('id_movie_theater', 'name', 'capacity')
    search_fields = ('name',)
    list_filter = ('capacity',)