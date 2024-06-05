from django.contrib import admin
from .models import Film, Format

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'duration', 'release_date')
    search_fields = ('name', 'genre')
    filter_horizontal = ('formats',)  # Esto permite mostrar los formatos en una vista de múltiples selecciones

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
