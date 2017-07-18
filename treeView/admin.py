# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import treeView


class ContinentFilter(admin.SimpleListFilter):
    title = 'continent'
    parameter_name = 'continent'

    def lookups(self, request, model_admin):
        continents = treeView.objects.filter(level=1).order_by('name')

        return [(c.name,c.name) for c in continents]

    def queryset(self, request, queryset):
        value = self.value()

        if not value:
            return queryset
        else:
            continent = treeView.objects.get(name=value,level=1)

            return continent.get_descendants(include_self=True)

class treeViewAdmin(DjangoMpttAdmin):
    tree_auto_open = 0
    list_display = ('id','name')
    ordering = ('name',)
    list_filter = (ContinentFilter,)

    # function: change TreeNode permission
    #def has_change_permission(self, request, obj=None):
        #return request.user.is_superuser

admin.site.register(treeView, treeViewAdmin)
