from django.shortcuts import render
from .models import Movie
from .filters import MovieFilter


def index(request):
    movies = Movie.objects.all()
    myFilter = MovieFilter(request.GET, queryset=movies)
    movies = myFilter.qs
    context = {
        'myFilter': myFilter,
        'movies': movies,
    }
    return render(request, 'movielist\index.html', context)
