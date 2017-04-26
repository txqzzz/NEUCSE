# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from .models import treeView


# Create your views here.



def tree(request):
    nodes = treeView.objects.all()
    return render_to_response("treeView.html", {'nodes': nodes})