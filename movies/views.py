from django.db.models import Count, Avg
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer, MovieStatsSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review
# Create your views here.


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        else:
            return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):

    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        avg_stars = round(Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars'], 1)

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'avg_stars': avg_stars
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
