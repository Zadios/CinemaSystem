from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Movie_Theater, Price, Show, Ticket, Format, Language, Film

@admin.register(Movie_Theater)
class MovieTheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'get_movie_theater_formats', 'id_movie_theater')
    search_fields = ('name',)
    list_filter = ('capacity',)
    
    def get_movie_theater_formats(self, obj):
        return ", ".join([format.name for format in obj.formats.all()]) if obj.formats.exists() else '-'
    
    get_movie_theater_formats.short_description = 'Formatos compatibles'

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'ticket_quantity', 'id_price')
    search_fields = ('name',)
    list_filter = ('amount',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('show_code', 'film', 'movie_theater', 'show_date', 'show_time', 'format', 'language')
    search_fields = ('name',)
    list_filter = ('show_date', 'movie_theater')

    # Sobrescribimos el método save para agregar validaciones personalizadas
    def save_model(self, request, obj, form, change):
        # Verificar que el formato pertenece a los formatos de la película
        if obj.format not in obj.film.format.all():
            raise ValidationError(f"El formato {obj.format} no está disponible para la película {obj.film.name}.")

        # Verificar que el lenguaje pertenece a los lenguajes de la película
        if obj.language not in obj.film.language.all():
            raise ValidationError(f"El lenguaje {obj.language} no está disponible para la película {obj.film.name}.")
        
        super().save_model(request, obj, form, change)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'show_code', 'price', 'ticket_quantity')
    search_fields = ('ticket_code',)
    list_filter = ('show_code', 'price')

