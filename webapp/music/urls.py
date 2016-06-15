from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$',views.IndexView.as_view(),name="index"),

    #/music/#id
    url(r'^(?P<artist>.+)/(?P<album_title>.+)/$',views.DetailView.as_view(), name="details"),

    #music/album/add
    url(r'album/add$', views.AlbumCreate.as_view(),name='album-add'),

    url(r'^(?P<artist>.+)/(?P<album_title>.+)/update/$', views.AlbumUpdate.as_view(),name='album-update'),

    url(r'^(?P<artist>.+)/(?P<album_title>.+)/delete/$', views.AlbumDelete.as_view(),name='album-delete')

]
