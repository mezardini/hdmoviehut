from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('movies/', views.movies, name="movies"),
    path('movies/results', views.movie_filter, name="movieFilter"),
    path('movie/<str:pk>/', views.movie, name="movie"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    