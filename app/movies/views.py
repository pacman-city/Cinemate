from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Movie


class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


# class MovieView(View):
#     """Список фильмов"""
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html',
#                       {'movie_list': movies})


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'url'
