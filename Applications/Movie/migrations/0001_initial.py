# Generated by Django 5.0.4 on 2024-05-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrenos', models.CharField(max_length=50, verbose_name='Nuevo Estreno')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nombre')),
                ('shor_name', models.CharField(default='', max_length=20, verbose_name='Codigo pelicula')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
            options={
                'verbose_name': 'Ranking',
                'verbose_name_plural': 'Ranking',
                'ordering': ['-name'],
                'unique_together': {('name', 'shor_name')},
            },
        ),
    ]
