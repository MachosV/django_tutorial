from django.conf.urls import url
from . import views

app_name = 'work_as'

urlpatterns = [
    url(r'^$',views.login,name="login"),
    url(r'^login',views.login,name="login"),
    url(r'^main',views.main.as_view(),name="main"),
    url(r'^parts',views.parts.as_view(),name="parts"),
    url(r'^newPart',views.createPart.as_view(),name="newPart"),
    url(r'search',views.search,name="search"),
    url(r'details/part/(?P<part_code>.+)',views.partDetail.as_view(),name="partDetail")
    ]