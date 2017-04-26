# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import treeView
# Register your models here.



class treeViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'level')

admin.site.register(treeView, treeViewAdmin)