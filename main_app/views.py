from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tape, Movie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

@login_required
def tapes_index(request):
  tapes = Tape.objects.filter(user=request.user)
  return render(request, 'tapes/index.html', {
    'tapes': tapes
  })



class TapeCreate(LoginRequiredMixin, CreateView):
  model = Tape
  fields = ['name', 'quantity', 'quality']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    # Edward: this needs to eventually be
    return super().form_valid(form)
    # it was causing and error though 
    # return redirect('index')

@login_required
def tapes_detail(request, tape_id):
  tape = Tape.objects.get(id=tape_id)
  id_list = tape.movies.all().values_list('id')
  movies_tape_doesnt_have = Movie.objects.exclude(id__in=id_list)
  return render(request, 'tapes/detail.html', {
    'tape': tape, 'movies' : movies_tape_doesnt_have
  })

class TapeUpdate(LoginRequiredMixin, UpdateView):
  model = Tape
  fields = ['quantity', 'quality']


class TapeDelete(LoginRequiredMixin, DeleteView):
  model = Tape
  success_url ='/tapes'


class MovieList(LoginRequiredMixin, ListView):
  model = Movie
  

class MovieDetail(LoginRequiredMixin, DetailView):
  model = Movie


class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = '__all__'


class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies'

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = '__all__'
  success_url ='/movies'

@login_required
def assoc_movie(request, tape_id, movie_id):
  Tape.objects.get(id=tape_id).movies.add(movie_id)
  return redirect('detail', tape_id=tape_id)

@login_required
def unassoc_movie(request, tape_id, movie_id):
  Tape.objects.get(id=tape_id).movies.remove(movie_id)
  return redirect('detail', tape_id=tape_id)


@login_required
def search_media(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    movies = Movie.objects.filter(title__contains=searched, director_contains=searched)
    # director =  Movie.objects.filter(director_contains=searched)
    # tapes_name =  Tape.objects.filter(name_contains=searched)
    return render(request, 'search_results.html', {
      'searched': searched, 'movies': movies,
    })
  else:
    return render(request, 'search_results.html', {})

