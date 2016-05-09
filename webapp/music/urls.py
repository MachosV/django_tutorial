from django.conf.urls import url
from . import views


urlpatterns = [
    #/music/
    url(r'^$',views.index,name="index"),

    #/music/#id
    url(r'^(?P<artist>.+)/(?P<album_title>.+)/$',views.details, name="details")
]
