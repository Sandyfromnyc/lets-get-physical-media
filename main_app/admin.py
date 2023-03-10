from django.contrib import admin
from .models import Tape, Movie
from .models import Collector

# Register your models here.
admin.site.register(Tape)
admin.site.register(Movie)
admin.site.register(Collector)