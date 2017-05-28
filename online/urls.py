from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'online'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^verify/(\d+)/(\d+)/$', views.verify, name='verify'),
    url(r'^check/$', views.check, name='check'),
    url(r'^temp/$', views.temp)
]
