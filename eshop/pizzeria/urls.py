from django.conf.urls import url
from . import views

app_name = 'pizzeria'

urlpatterns = [
    #/music/
    url(r'^$',views.IndexView.as_view(),name="index"),