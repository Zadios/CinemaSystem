# Generated by Django 5.0.4 on 2024-10-13 21:58

import Applications.Showtime.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showtime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_code',
            field=models.CharField(default=Applications.Showtime.utils.generate_ticket_code, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
