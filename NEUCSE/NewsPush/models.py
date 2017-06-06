from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(NewsPost,NewsPostAdmin)