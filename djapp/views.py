from django.shortcuts import render, get_object_or_404
from .models import Performer, Track, Genre, Album


def performers_list(request):
    artists = Performer.objects.all()
    return render(request, 'djapp/index.html', {'artists': artists})


def info_by_artist(request, artist_name):
    artist = get_object_or_404(Performer, name=artist_name)

    albums = artist.Albums.all()
    for album in albums:
        tracks = album.tracks.all()
        for genre in tracks:
            genre.track.all()

    return render(request, 'djapp/artists_list.html', {
                'artist': artist,
                'albums': albums,
            })


def sort_alfabet(request):

    artists = Performer.objects.order_by('name')
    return render(request, 'djapp/index.html', {'artists': artists})


def sort_vise(request):

    artists = Performer.objects.order_by('-name')
    return render(request, 'djapp/index.html', {'artists': artists})


def find_songs(request, genre_name):

    tracks_obj = get_object_or_404(Genre, genre =genre_name)
    tracks_list = tracks_obj.track.all()

    return render(request, 'djapp/track_list.html', {
        'genre': genre_name,
        'tracks': tracks_list,
    })