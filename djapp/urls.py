from django.contrib import admin
from django.urls import path

from . import views

#?
urlpatterns = [
    path('', views.performers_list, name='performers_list'),
    path('<str:artist_name>/', views.info_by_artist, name='artist'),
    path('index/<str:genre_name>/', views.find_songs, name='tracks_list'),
    path('index/1', views.sort_alfabet, name='sort_alfabet'),
    path('index/1/1', views.sort_vise, name='sort_vise'),
]