# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # useremail =
    # username = models.CharField (max_length= 50)
    # password = models.CharField (max_length =50)
    userrank = models.IntegerField (default=0)
    #useremail = models.EmailField (max_length =75)

    #def __unicode__(self):
        #return self.username


class UserAdmin(admin.ModelAdmin):
    #list_display = ('username', 'userrank', 'useremail')
    list_display = ('user', 'userrank',)


def create_user_profile(sender,instance,created,**kwags):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)

admin.site.register(UserProfile,UserAdmin)

