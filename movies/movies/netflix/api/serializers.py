from rest_framework import serializers, viewsets, routers
from netflix.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ['id', 'title', 'desc', 'year' ,'poster', 'video']
        