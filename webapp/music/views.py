from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

    def get_object(self,queryset=None):
        artist = self.kwargs['artist']
        album_title = self.kwargs['album_title']
        return Album.objects.all().filter(artist=artist).filter(album_title=album_title)[0]

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')