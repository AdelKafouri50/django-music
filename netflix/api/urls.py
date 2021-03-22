from django.urls import path
from .views import index, create, MovieList, CreateMovie

urlpatterns = [
    path('', index),
    path('create', create),
    path('list/', MovieList.as_view()),
    path('add/', CreateMovie.as_view())
]