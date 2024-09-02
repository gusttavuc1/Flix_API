from django.urls import path
from . import views
from .views import genre_view

urlpatterns = [
    path('genres/', genre_view, name='genre_list'),
    # Adicione outras URLs do aplicativo aqui
]