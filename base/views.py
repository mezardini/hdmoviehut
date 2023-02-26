from django.shortcuts import render
from .models import Movie, Comment
from .filters import MovieFilter
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    movies = Movie.objects.filter(status='Released')
    movies_exp = Movie.objects.filter(status='Expected')
    

    context = {'movies':movies, 'movies_exp':movies_exp}
    return render(request, 'index.html', context)



def movie(request, pk):
    movies = Movie.objects.get(id=pk)
    movie = Movie.objects.all

    context = {'movies':movies, 'movie':movie}
    return render(request, 'details.html', context,)

def movies(request):
    movies = Movie.objects.filter(status='Released') 
    movie_type = MovieFilter(request.GET, queryset=movies)
    form = MovieFilter()

    prop_pagi = Paginator(movies, 2 )

    page_num = request.GET.get('page')

    page = prop_pagi.get_page(page_num)


    context = {'movies':movies,'form':form, 'movie':movie_type, 'page':page, 'count':prop_pagi.count}
    return render(request, 'moviescatalog.html', context)

def movie_filter(request):
    movies = Movie.objects.filter(status='Released') 
    movie_type = MovieFilter(request.GET, queryset=movies)

    context = {'movies':movies, 'movie_type':movie_type }
    return render(request, 'search_catalog.html', context)
