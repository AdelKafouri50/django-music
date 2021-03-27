from django.urls import path
from .views import index, create, MovieList, CreateMovie, api_signup
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sign_up/', api_signup),
    path('login/', obtain_auth_token),
    path('', index),
    path('create/', create),
    path('list/', MovieList.as_view()),
    path('add/', CreateMovie.as_view())
]