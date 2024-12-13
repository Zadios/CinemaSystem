import os
from django.db import models
from django.conf import settings

# Modelos para la aplicación

class Format(models.Model):
    id_format = models.AutoField(primary_key=True)
    name = models.CharField('Formato', max_length=20, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField('Género', unique=True)

    def __str__(self):
        return self.name


class Age_Restriction(models.Model):
    id_age_restriction = models.AutoField(primary_key=True)
    name = models.CharField('Restricción de edad (código)', max_length=4, unique=True)
    number = models.IntegerField('Restricción numérica', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restricción de edad"
        verbose_name_plural = "Restricciones de edad"


class Language(models.Model):
    id_language = models.AutoField(primary_key=True)
    name = models.CharField('Lenguaje', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"


class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=True)
    synopsis = models.TextField('Sinopsis', null=True)
    image = models.ImageField('Imagen', upload_to='covers/', null=True, blank=True) 
    duration = models.IntegerField('Duración', null=True)
    release_date = models.DateField('Fecha de Lanzamiento', null=True, blank=True)
    upcoming_releases = models.BooleanField('Próximos Lanzamientos', default=False)
    trailer_link = models.CharField('Enlace tráiler de YouTube', max_length=255, null=True)
    language = models.ManyToManyField(Language)
    age_restriction = models.ForeignKey('Movie.Age_Restriction', on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField('Movie.Genre')
    format = models.ManyToManyField(Format)

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        # Si la película tiene una imagen, eliminamos el archivo de imagen
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        # Llamamos al método delete() original para eliminar el registro de la base de datos
        super().delete(*args, **kwargs)

class Banner(models.Model):
    id_banner = models.AutoField(primary_key=True)
    order = models.PositiveIntegerField('Orden', default=0)
    description = models.CharField('Descripción', max_length=30, null=True)
    image = models.ImageField('Imagen', upload_to='bannerImages/', null=True, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def save(self, *args, **kwargs):
        if self.pk is None:  # Si el banner es nuevo
            # Empujar banners existentes hacia adelante si tienen la misma prioridad o superior
            Banner.objects.filter(order__gte=self.order).update(order=models.F('order') + 1)
        else:  # Si es una actualización de un banner existente
            original_order = Banner.objects.get(pk=self.pk).order
            if self.order != original_order:
                if self.order > original_order:  # Si el nuevo orden es mayor
                    Banner.objects.filter(order__gt=original_order, order__lte=self.order).update(order=models.F('order') - 1)
                else:  # Si el nuevo orden es menor
                    Banner.objects.filter(order__gte=self.order, order__lt=original_order).update(order=models.F('order') + 1)

        super().save(*args, **kwargs)  # Guardar el banner

    def __str__(self):
        return f"Banner {self.id_banner}: {self.description if self.description else 'Sin descripción'}"
