# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'treeView'
urlpatterns = [
    url(r'^(?P<page_name>.+).html/$', views.uniform_page, name='uniform'),
]
