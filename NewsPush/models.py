#encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    author = models.CharField(max_length=50,verbose_name="作者")
    cover = models.ImageField(upload_to='Img',verbose_name="封面图")
    body = RichTextUploadingField(blank=True, null=True, verbose_name="内容")
    timestamp = models.DateTimeField(verbose_name="发布时间")
    headline = models.CharField(max_length=50,default="",verbose_name="摘要")


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(NewsPost,NewsPostAdmin)