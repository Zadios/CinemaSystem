from django.db import models
from Applications.Movie.models import Format, Film, Language
from .utils import generate_ticket_code


class Movie_Theater(models.Model):
    id_movie_theater = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    capacity = models.PositiveIntegerField('Capacidad', null=True)
    formats = models.ManyToManyField(Format)

    def __str__(self):
        return self.name

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
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)  # Añadimos formato
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)  # Añadimos lenguaje

    class Meta:
        unique_together = ('film', 'show_date', 'show_time')  # Asegura que no haya dos funciones iguales
        ordering = ['show_date', 'show_time']  # Ordena por fecha y hora

    def __str__(self):
        return f"{self.film.name} - {self.show_date} {self.show_time}"


class Ticket(models.Model):
    ticket_code = models.CharField(default=generate_ticket_code, max_length=8, primary_key=True, editable=False)
    show_code = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)
    ticket_quantity = models.PositiveIntegerField('Cantidad de entradas')

    def __str__(self):
        return f"Ticket {self.ticket_code} - {self.ticket_quantity} entradas para {self.show_code}"