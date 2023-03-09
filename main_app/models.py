from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  imdb_id = models.CharField(max_length=100)
  year = models.CharField(max_length=6)
  released = models.CharField(max_length=50)
  rated = models.CharField(max_length=7)
  runtime = models.CharField(max_length=20)
  genre = models.CharField(max_length=150)
  director = models.CharField(max_length=100)
  writer = models.CharField(max_length=100)
  actors = models.CharField(max_length=300)
  plot = models.CharField(max_length=300)
  poster = models.CharField(max_length=300)
  language = models.CharField(max_length=300)
  country = models.CharField(max_length=300)
  type_media = models.CharField(max_length=100)
  box_office = models.CharField(max_length=100)
  imdb_rating = models.CharField(max_length=100)
  awards = models.CharField(max_length=100)

class Tape(models.Model):
  title = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  quantity = models.IntegerField()
  quality = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  format = models.CharField(max_length=30)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'tape_id': self.id})