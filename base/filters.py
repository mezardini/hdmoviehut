import django_filters
from django_filters import RangeFilter, FilterSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    genre = {'genre': ['exact']}
    industry = {'industry': ['exact']}
    rating = {'rating': ['exact']}
    class Meta:
        model = Movie
        fields = ['rating', 'genre', 'industry', 'release_year']


