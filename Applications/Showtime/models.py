from django.db import models
from Applications.Movie.models import Format, Film, Language
from django.core.exceptions import ValidationError
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
    available_seats = models.PositiveIntegerField(default=0)  # Campo para asientos disponibles
    show_date = models.DateField()
    show_time = models.TimeField()
    prices = models.ManyToManyField(Price)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('film', 'show_date', 'show_time')
        ordering = ['show_date', 'show_time']

    def __str__(self):
        return f"{self.film.name} - {self.show_date} {self.show_time}"
    
    def clean(self):
        super().clean()
        # Validación del formato
        if self.film and self.film.format.filter(id_format=self.format.id_format).count() == 0:
            raise ValidationError(f"El formato {self.format} no está disponible para la película {self.film.name}.")
        
        # Validación del lenguaje
        if self.film and self.film.language.filter(id_language=self.language.id_language).count() == 0:
            raise ValidationError(f"El lenguaje {self.language} no está disponible para la película {self.film.name}.")

    def save(self, *args, **kwargs):
        # Si es una nueva instancia, inicializar available_seats con la capacidad de la sala
        if self.pk is None and self.movie_theater:
            self.available_seats = self.movie_theater.capacity
        super().save(*args, **kwargs)

class Ticket(models.Model):
    ticket_code = models.CharField(max_length=20, unique=True)
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    total_tickets = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField('Estado', default=True)

    def save(self, *args, **kwargs):
        # Actualizar los asientos disponibles en el show
        if self.pk is None:  # Solo al crear un nuevo ticket
            if self.show.available_seats < self.total_tickets:
                raise ValueError("No hay suficientes asientos disponibles para esta función.")
            self.show.available_seats -= self.total_tickets
            self.show.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.ticket_code} for {self.show}"
    
class Ticket_Price(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name="purchased_prices")
    price = models.ForeignKey('Price', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.price.name} for Ticket {self.ticket.ticket_code}"