from .models import MovieShow
from rest_framework import serializers


class MovieShowSerializers(serializers.ModelSerializer):
    """Serializer for all Movie show"""
    class Meta:
        model = MovieShow
        fields = '__all__'


class TotalMovieTvSerializers(serializers.ModelSerializer):
    """Serializer for total_movie and total_tv_show"""

    total_movie = serializers.IntegerField()
    total_tv_show = serializers.IntegerField()

    class Meta:
        model = MovieShow
        fields = ('total_movie', 'total_tv_show')