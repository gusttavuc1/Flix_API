from django.urls import path
from . import views


app_name = 'genres'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='GenreCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='GenreRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]
