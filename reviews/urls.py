from django.urls import path
from .views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', ReviewCreateListView.as_view(), name='ReviewCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='ReviewRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]