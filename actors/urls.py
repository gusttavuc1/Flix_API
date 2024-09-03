from django.urls import path
from .views import ActorCreateListView, ActorRetrieveUpdateDestroyView


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', ActorCreateListView.as_view(), name='ActorCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='ActorRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]