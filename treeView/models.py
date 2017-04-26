# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mptt.models import MPTTModel


# Create your models here.




class treeView(MPTTModel):
    name = models.CharField('root', max_length=50, unique=True)
    parent = models.ForeignKey('self', verbose_name='lower-case', null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'treeView'
        verbose_name = verbose_name_plural = 'treeViewList'

    def __unicode__(self):
        return self.name