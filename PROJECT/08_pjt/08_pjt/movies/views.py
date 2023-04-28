from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from django.views.decorators.http import require_safe
from .models import Movie,Genre
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MovieListSerializer,MovieDetailSerializer
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
@require_safe
def index(request):
    if request.method == 'GET' :        
        movies = get_list_or_404(Movie)
        context = {
            'movies' : movies,
        }
        return render(request,'movies/index.html',context)
        

def detail(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  genres = movie.genres.all()
  context = {
      'movie' : movie,
      'genres' : genres,
  }
  return render(request,'movies/detail.html',context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        recommended_movies = []
        movies = Movie.objects.all()
        for movie in movies :
            if len(recommended_movies) == 10 :
                break
            
            if movie.vote_average > 8.5 :
                recommended_movies.append(movie)
        context = {
            'recommended_movies' : recommended_movies,
        }                        
        return render(request,'movies/recommended.html',context)
    return redirect('movies:index')