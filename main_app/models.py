from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=100)
  director = models.CharField(max_length=100)


class Tape(models.Model):
  name = models.CharField(max_length=100)
  quantity = models.IntegerField()
  quality = models.CharField(max_length=100)
  movies = models.ManyToManyField(Movie)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'tape_id': self.id})