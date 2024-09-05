from django.urls import path
from . import views


app_name = 'actors'  # Opcional, mas útil para namespaces

urlpatterns = [
    path('', views.MovieCreateListView.as_view(), name='MovieCreateListView'),  # Página inicial para 'genres'
    path('<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='MovieRetrieveUpdateDestroyView'),
    path('stats/', views.MovieStatsView.as_view(), name='MovieStatsView'),
    # Detalhes de um gênero específico
    # Adicione outras URLs do aplicativo aqui
]
