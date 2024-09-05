from django.contrib import admin
from .models import Movie
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'display_actors', 'resumo')

    def display_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])
    display_actors.short_description = 'Actors'
