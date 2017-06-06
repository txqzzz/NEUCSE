# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models


class User(models.Model):
    username = models.CharField (max_length= 50)
    password = models.CharField (max_length =50)
    userrank = models.IntegerField (null=True)
    useremail = models.EmailField (max_length =75)

    def __unicode__(self):
        return self.username


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'userrank', 'useremail')

admin.site.register(User,UserAdmin)