from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="myMovies/posters")
    video = models.FileField(upload_to="myMovies/video")




