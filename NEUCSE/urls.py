# -*- coding: utf-8 -*-
"""NEUCSE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from treeView import views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^treeView/', views.tree, name='tree'),
    url(r'^treeView/', include('treeView.urls')),

    url(r'^$', views.index, name='index'),
    url(r'newspush/', include('NewsPush.urls', namespace='NewsPush')),
    url(r'^online/',include('online.urls', namespace='online')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
#    url(r'^组织结构.html', views., name='index'),
#    url(r'^$/组织结构.html/', views.institude, name='institude'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
