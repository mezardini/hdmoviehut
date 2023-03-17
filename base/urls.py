from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('movies/', views.movies, name="movies"),
    path('movies/<str:genre>/', views.genre, name="genre"),
    path('movies/results', views.movie_filter, name="movieFilter"),
    path('movie/<str:pk>/', views.movie, name="movie"),
    path('pay', views.pay, name='payment'),
    path('search-result', views.search, name="search"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    