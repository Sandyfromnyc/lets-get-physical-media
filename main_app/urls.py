from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tapes/', views.tapes_index, name='index'),
    path('tapes/create/', views.TapeCreate.as_view(), name="tapes_create"),
    path('tapes/<int:tape_id>/', views.tapes_detail, name='detail'),
    path('tapes/<int:pk>/update', views.TapeUpdate.as_view(), name='tapes_update'),
    path('tapes/<int:pk>/delete', views.TapeDelete.as_view(), name='tapes_delete'),
    path('tapes/<int:tape_id>/assoc_movie/<int:movie_id>/', views.assoc_movie, name='assoc_movie'),
    path('tapes/<int:tape_id>/unassoc_movie/<int:movie_id>/', views.unassoc_movie, name='unassoc_movie'),
    path('movies/', views.MovieList.as_view(), name="movies_index"),
    path('movies/create/', views.MovieCreate.as_view(), name="movies_create"),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name="movies_detail"),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movies_update"),
    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="movies_delete"),
]
	