from django.db.models import Avg
from rest_framework import serializers
from .models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField(child=serializers.DictField())
    total_reviews = serializers.IntegerField()
    avg_stars = serializers.FloatField()


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()    
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))['stars__avg']

        if rate:
            return round(rate, 1)
        return None