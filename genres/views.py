from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermissions


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Sem usar DRF
# Create your views here.
""" @csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name = data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201,)
 """

""" @csrf_exempt
def genre_detail_view(request, pk):
    try:
        genre = get_object_or_404(Genre, pk=pk)
    except Exception as e:
        print(f"Error finding genre: {e}")
        return JsonResponse({'error': 'Genre not found'}, status=404)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data.get('name')
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name})

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Genero Excluido com sucesso.'}, status=204,) """
