from django.contrib import admin

# Register your models here.
from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    