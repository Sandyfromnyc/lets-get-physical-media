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

def tapes_detail(request, tape_id):
  tape = Tape.objects.get(id=tape_id)

  return render(request, 'tapes/detail.html', {
    'tape': tape, 
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
  fields = 'director'


class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies'

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = '__all__'
