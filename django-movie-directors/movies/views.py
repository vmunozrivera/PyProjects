
from django.views.generic import ListView, DetailView

from .models import Director, Movie


class DirectorListView(ListView):
    template_name = 'director-list.html'
    model = Director


class DirectorDetailView(DetailView):
    template_name = 'director-detail.html'
    model = Director


class MovieDetailView(DetailView):
    template_name = 'movie-detail.html'
    model = Movie
