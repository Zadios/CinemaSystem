# Generated by Django 5.0.4 on 2024-12-12 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_alter_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
    ]
