from importlib.util import module_from_spec
from django.db import models

# Create your models here.

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100, null=True)
    sinopsis = models.TextField('Sinopsis', null=True)
    imagen = models.ImageField('Imagen', upload_to='portadas/', null=True, blank=True)
    duracion = models.IntegerField('Duración', null=True)
    genero = models.CharField('Género', max_length=50, null= True)

    def __str__(self):
        return str(self.id)+ ' - ' + self.nombre