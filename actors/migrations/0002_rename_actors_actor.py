# Generated by Django 5.1 on 2024-09-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actors',
            new_name='Actor',
        ),
    ]
