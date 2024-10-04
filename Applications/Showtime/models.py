from django.db import models
from Applications.Movie.models import Format, Film
import uuid

class Movie_Theater(models.Model):
    id_movie_theater = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    capacity = models.PositiveIntegerField('Capacidad', null=True)
    formats = models.ManyToManyField(Format)

class Price(models.Model):
    id_price = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la Promoción', max_length=100)
    amount = models.PositiveIntegerField('Precio')
    ticket_quantity = models.PositiveIntegerField('Cantidad de entradas')

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'

    def __str__(self):
        return f"{self.name}: {self.amount} (Cantidad: {self.ticket_quantity})"


class Show(models.Model):
    show_code = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    movie_theater = models.ForeignKey(Movie_Theater, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    prices = models.ManyToManyField(Price)

    class Meta:
        unique_together = ('film', 'show_date', 'show_time')  # Asegura que no haya dos funciones iguales
        ordering = ['show_date', 'show_time']  # Ordena por fecha y hora

    def __str__(self):
        return f"{self.film.title} - {self.show_date} {self.show_time}"

class Ticket(models.Model):
    ticket_code = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)  # Código único del ticket
    show_code = models.ForeignKey(Show, on_delete=models.CASCADE)  # Relación con Show
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)  # Relación con Price
    ticket_quantity = models.PositiveIntegerField('Cantidad de entradas')  # Cantidad de entradas compradas

    def __str__(self):
        return f"Ticket {self.ticket_code} - {self.ticket_quantity} entradas para {self.show_code}"