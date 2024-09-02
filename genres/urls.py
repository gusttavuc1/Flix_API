from django.urls import path
from .views import genre_create_list_view, genre_detail_view


app_name = 'genres'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', genre_create_list_view, name='index'),  # Página inicial para 'genres'
    path('<int:pk>/', genre_detail_view, name='genre_detail_view'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]