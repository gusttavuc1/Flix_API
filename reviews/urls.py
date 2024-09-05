from django.urls import path
from . import views


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', views.ReviewCreateListView.as_view(), name='ReviewCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='ReviewRetrieveUpdateDestroyView'),  # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]
