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


def detail(request,album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album
    }
    return render(request, 'music/details.html', context)