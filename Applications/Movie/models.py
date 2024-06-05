from importlib.util import module_from_spec
from django.db import models

# Create your models here.

class Format(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Film(models.Model):

    GENRE_CHOICES = [
        ('Acción', 'Acción'),
        ('Aventura', 'Aventura'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('No-Ficción', 'No-Ficción'),
        ('Drama', 'Drama'),
        ('Fantasía', 'Fantasía'),
        ('Musical', 'Musical'),
        ('Suspense', 'Suspense'),
        ('Terror', 'Terror'),
        ('Comedia', 'Comedia'),

    ]

    AGE_RESTRICTION_CHOICES = [
        ('0', 'G'),
        ('7', 'PG'),
        ('13', 'PG-13'),
        ('17', 'R'),
        ('18', 'NC-17'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    synopsis = models.TextField('Sinopsis', null=True)
    image = models.ImageField('Imagen', upload_to='covers/', null=True, blank=True)
    duration = models.IntegerField('Duración', null=True)
    genre = models.CharField('Género', max_length=30, choices=GENRE_CHOICES, default='')
    subgenre = models.CharField('Subgénero', max_length=30, choices=GENRE_CHOICES, default='', blank=True, null=True)
    formats = models.ManyToManyField(Format, verbose_name='Formato', related_name='films')
    release_date = models.DateField('Fecha de Lanzamiento', null=True, blank=True)
    age_restriction = models.CharField('Restricción Edad', max_length=2, choices=AGE_RESTRICTION_CHOICES)

    def __str__(self):
        return f"{self.id} - {self.name}"