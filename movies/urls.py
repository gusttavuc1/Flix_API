from django.urls import path
from .views import MovieCreateListView, MovieRetrieveUpdateDestroyView


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', MovieCreateListView.as_view(), name='MovieCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='MovieRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]