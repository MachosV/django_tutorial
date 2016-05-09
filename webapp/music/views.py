from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

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