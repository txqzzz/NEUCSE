# coding=utf-8
from django.conf.urls import url,include
from django.contrib import admin



from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newspush/(?P<news_list_id>[0-9]+)$', views.news_content_page, name='news_content_page'),
 #   url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
#    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]