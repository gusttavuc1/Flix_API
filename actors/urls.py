from django.urls import path
from . import views


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', views.ActorCreateListView.as_view(), name='ActorCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='ActorRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]