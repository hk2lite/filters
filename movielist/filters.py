import django_filters
from .models import Movie
from django_filters import CharFilter


class MovieFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['title']
