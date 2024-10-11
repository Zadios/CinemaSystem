from django.contrib import admin
from .models import Movie_Theater, Price, Show, Ticket, Format, Film

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
    list_display = ('show_code', 'film', 'movie_theater', 'show_date', 'show_time','get_film_format', 'get_film_language')
    search_fields = ('name',)
    list_filter = ('show_date', 'movie_theater')

    def get_film_format(self, obj):
        return obj.film.format if obj.film else '-'
    get_film_format.short_description = 'Formato'

    def  get_film_language(self, obj):
        return obj.film.language if obj.film else '-'
    get_film_language.short_description = 'Idioma'

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'show_code', 'price', 'ticket_quantity')
    search_fields = ('ticket_code',)
    list_filter = ('show_code', 'price')

