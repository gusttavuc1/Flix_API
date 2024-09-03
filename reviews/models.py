from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação deve ser maior ou igual a 0 estrelas'),
            MaxValueValidator(5, 'Avaliação deve ser menor ou igual a 5 estrelas')
        ]
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f"{self.movie.title} - {self.stars} stars"