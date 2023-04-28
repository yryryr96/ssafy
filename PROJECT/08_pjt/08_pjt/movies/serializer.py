from rest_framework import serializers
from .models import Movie,Genre

class MovieListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Movie
        fields = ("title","vote_average",)
        
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = Movie
        fields = '__all__'