# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render
from treeView.models import treeView


# Create your views here.



def tree(request):
    nodes = treeView.objects.all()
    return render_to_response("treeView.html", {'nodes': nodes})


def index(request):
    nodes = treeView.objects.all()
    return render_to_response("index.html", {'nodes': nodes})


def institude(request):
    nodes = treeView.objects.all()
    return render_to_response("组织机构.html", {'nodes': nodes})


def uniform_page(request, page_name):
    nodes = treeView.objects.all()
    page = page_name + '.html'
    return render_to_response(page, {'nodes': nodes})
