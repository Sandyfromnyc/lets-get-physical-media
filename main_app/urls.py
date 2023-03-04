from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tapes/', views.tapes_index, name='index'),
    path('tapes/create/', views.TapeCreate.as_view(), name="tape_create"),
    path('tapes/<int:tape_id>/', views.tapes_detail, name='detail'),
    path('tapes/<int:pk>/update', views.TapeUpdate.as_view(), name='tapes_update'),
    path('tapes/<int:pk>/delete', views.TapeDelete.as_view(), name='tapes_delete'),
]
	