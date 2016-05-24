from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Song

# Create your views here.


def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'music/index.html', context)


def details(request,artist,album_title):
    try:
        album = Album.objects.filter(album_title=album_title).filter(artist=artist)[0]
        context = {
            'album': album
        }
        return render(request, 'music/details.html', context)
    except:
        return HttpResponse("Album does not exist :(")


def favorite(request, artist, album_title):
    album = Album.objects.filter(album_title=album_title).filter(artist=artist)[0]
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExit):
        return render(request, 'music/detalis.html', {
            'album': album,
            'error_msg': 1
        })
    else:
        selected_song.is_favorite = not selected_song.is_favorite
        selected_song.save()
    return render(request, 'music/details.html', {'album': album})
