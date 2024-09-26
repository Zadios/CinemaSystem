from django.contrib import admin
from .models import Film, Format, Genre, Age_Restriction, Language

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('id_format', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id_genre', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Age_Restriction)
class AgeRestrictionAdmin(admin.ModelAdmin):
    list_display = ('id_age_restriction', 'name', 'number')
    search_fields = ('name', 'number')
    list_filter = ('number',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id_language', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id_film', 'name', 'release_date', 'language', 'upcoming_releases')
    search_fields = ('name', 'release_date')
    list_filter = ('release_date', 'upcoming_releases', 'language')