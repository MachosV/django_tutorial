from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$',views.index,name="index"),

    #/music/#id
    url(r'^(?P<artist>.+)/(?P<album_title>.+)/$',views.details, name="details"),

    url(r'^(?P<artist>.+)/(?P<album_title>.+)/favorite$',views.favorite, name="favorite")
]
