# Generated by Django 5.0.4 on 2024-10-04 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age_Restriction',
            fields=[
                ('id_age_restriction', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4, unique=True, verbose_name='Restricción de edad (código)')),
                ('number', models.IntegerField(unique=True, verbose_name='Restricción numérica')),
            ],
            options={
                'verbose_name': 'Restricción de edad',
                'verbose_name_plural': 'Restricciones de edad',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id_format', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Formato')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_genre', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Género')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id_language', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Lenguaje')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id_film', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('synopsis', models.TextField(null=True, verbose_name='Sinopsis')),
                ('image', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Imagen')),
                ('duration', models.IntegerField(null=True, verbose_name='Duración')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Lanzamiento')),
                ('upcoming_releases', models.BooleanField(default=False, verbose_name='Próximos Lanzamientos')),
                ('trailer_link', models.CharField(null=True, verbose_name='Enlace tráiler de YouTube')),
                ('age_restriction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.age_restriction')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.format')),
                ('genres', models.ManyToManyField(to='Movie.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.language')),
            ],
        ),
    ]
