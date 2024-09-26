from importlib.util import module_from_spec
from django.db import models

# Create your models here.

class Format(models.Model):
    id_format = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=10, unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=10, unique=True)

    def __str__(self):
        return self.name
    
class Age_Restriction(models.Model):
    id_age_restriction = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=4, unique=True)
    number = models.IntegerField('Restricción numérica', unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    id_language = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=10, unique=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    synopsis = models.TextField('Sinopsis', null=True)
    image = models.ImageField('Imagen', upload_to='covers/', null=True, blank=True)
    duration = models.IntegerField('Duración', null=True)
    release_date = models.DateField('Fecha de Lanzamiento', null=True, blank=True)
    upcoming_releases = models.BooleanField('Próximos Lanzamientos', default=False)
    trailer_link = models.CharField('Enlace tráiler de YouTube', null=True)
    language = models.ForeignKey('Movie.Language', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_film} - {self.name}"
    



'''GENRE_CHOICES = [
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
    ('ATP', 'ATP'),
    ('13+', 'PM13'),
    ('16+', 'PM16'),
    ('18+', 'PM18'),
]'''