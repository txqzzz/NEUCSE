from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    # body = models.TextField()
    author =models.CharField(max_length=50)
    cover = models.ImageField(upload_to='Img')
    body = RichTextField(blank=True, null=True, verbose_name="Content")
    timestamp = models.DateTimeField()


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(NewsPost,NewsPostAdmin)