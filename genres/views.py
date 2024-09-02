from django.http import JsonResponse
from .models import Genre
# Create your views here.

def genre_view(request):
    genres = Genre.objects.all()
    return JsonResponse(genres)
    