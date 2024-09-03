from django.db import models

# Create your models here.

NATIONALITY_CHOICE = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil')
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, 
        choices=NATIONALITY_CHOICE,
        blank=True,
        null=True
        )
    def __str__(self):
        return self.name
    