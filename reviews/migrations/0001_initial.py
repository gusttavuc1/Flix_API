# Generated by Django 5.1 on 2024-09-03 19:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_alter_movie_resumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliação deve ser maior ou igual a 0 estrelas'), django.core.validators.MaxValueValidator(5, 'Avaliação deve ser menor ou igual a 5 estrelas')])),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movies.movie')),
            ],
        ),
    ]
