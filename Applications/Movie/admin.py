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

from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'upcoming_releases', 'get_languages', 'get_formats')
    search_fields = ('name',)
    list_filter = ('upcoming_releases', 'genres', 'age_restriction')

    def get_languages(self, obj):
        return ", ".join([lang.name for lang in obj.language.all()])
    get_languages.short_description = 'Idiomas'

    def get_formats(self, obj):
        return ", ".join([fmt.name for fmt in obj.format.all()])
    get_formats.short_description = 'Formatos'


