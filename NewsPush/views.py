from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import models
from treeView.models import treeView





def index(request):
     news_list = models.NewsPost.objects.all()
     nodes = treeView.objects.all()
     return render(request,'NewsPush/index.html', {'news_list': news_list, 'nodes': nodes})


def news_content_page(request,news_list_id):
    news = models.NewsPost.objects.get(pk=news_list_id)
    nodes = treeView.objects.all()
    return render(request,'NewsPush/news_content_page.html',{'news': news, 'nodes': nodes})
