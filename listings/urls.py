from django.conf.urls import patterns, url

from listings import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
)