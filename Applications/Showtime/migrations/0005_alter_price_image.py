# Generated by Django 5.0.4 on 2024-12-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showtime', '0004_price_description_price_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='image',
            field=models.ImageField(blank=True, default='static/img/CinemaRoyale.png', null=True, upload_to='promoIMG/', verbose_name='Imagen'),
        ),
    ]