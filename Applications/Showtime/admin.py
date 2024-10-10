from django.contrib import admin
from .models import Movie_Theater, Price, Show, Ticket

@admin.register(Movie_Theater)
class MovieTheaterAdmin(admin.ModelAdmin):
    list_display = ('id_movie_theater', 'name', 'capacity')
    search_fields = ('name',)
    list_filter = ('capacity',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id_price', 'name', 'amount', 'ticket_quantity')
    search_fields = ('name',)
    list_filter = ('amount',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('show_code', 'film', 'movie_theater', 'show_date', 'show_time')
    search_fields = ('name',)  # Asumiendo que Film tiene un campo title
    list_filter = ('show_date', 'movie_theater')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'show_code', 'price', 'ticket_quantity')
    search_fields = ('ticket_code',)
    list_filter = ('show_code', 'price')

