from django.urls import path
from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView


app_name = 'genres'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='GenreCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='GenreRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]