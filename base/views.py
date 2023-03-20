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
    movie = Movie.objects.get(id=pk)
    movies = Movie.objects.filter(status='Released') 
    comments = movie.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            author = request.POST['author'],
            rating = request.POST['rating'],
            movie = movies,
            text = request.POST['comment'],
        )
        comment.save()

    context = {'movies':movie, 'movie':movies, 'comments':comments}
    return render(request, 'details.html', context)

def genre(request, genre):
    movies = Movie.objects.filter(status='Released').filter(genre=genre)

    prop_pagi = Paginator(movies, 2 )

    page_num = request.GET.get('page')

    page = prop_pagi.get_page(page_num)

    context = {'movies':movies}
    return render(request, 'genre.html', context)

def payment(request, pk):
    movie = Movie.objects.get(id=pk)
    qprice = int(movie.price*100)
    price = "{:.0f}".format(qprice) 

    context = {'movie':movie, 'price':price}
    return render(request, 'payx.html', context)

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
    movies = Movie.objects.all()
    movie_type = MovieFilter(request.GET, queryset=movies)

    context = {'movies':movies, 'movie_type':movie_type }
    return render(request, 'search_catalog.html', context)

def pay(request):
    return render(request, 'payment.html')


def search(request):
    movie = Movie.objects.all()
    if request.method == 'GET':
        searched = request.GET['searched']
        topics = Movie.objects.filter(title__icontains = searched)
        return render(request, 'search_results.html', {'searched':searched,  'topics':topics, 'movie':movie})
    
