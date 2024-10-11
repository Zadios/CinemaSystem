from django.contrib import admin
from .models import Film, Format, Genre, Age_Restriction, Language

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_format')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_genre')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Age_Restriction)
class AgeRestrictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'id_age_restriction')
    search_fields = ('name', 'number')
    list_filter = ('number',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_language')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'language', 'upcoming_releases', 'format', 'id_film')
    search_fields = ('name', 'release_date')
    list_filter = ('release_date', 'upcoming_releases', 'language')

