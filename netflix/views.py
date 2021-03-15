from django.shortcuts import render, redirect
from .forms import  MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def index(request):
    movies = Movie.objects.all()

    return render(request, "netflix/index.html", {
        'movies': movies
    })

@login_required
def create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request, "netflix/create.html", {
        'form': form
    })

@login_required
def show(request, id):
    movie = Movie.objects.get(pk=id)

    return  render(request, "netflix/show.html", {
        "movie": movie
    })

@login_required
def delete(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('index')


