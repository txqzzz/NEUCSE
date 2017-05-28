# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render
from treeView.models import treeView


def index(request):
    nodes = treeView.objects.all()
    return render_to_response("index.html", {'nodes': nodes})


def uniform_page(request, page_name):
    nodes = treeView.objects.all()
    page = page_name + '.html'
    return render(request, page, {'nodes': nodes})
