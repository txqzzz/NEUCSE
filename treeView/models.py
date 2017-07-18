# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mptt.models import MPTTModel,TreeForeignKey


class treeView(MPTTModel):
    name = models.CharField('root', max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='lower-case',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'treeView'
        verbose_name = verbose_name_plural = 'treeViewList'

    class MPTTMeta:
        order_insertion_by = ['rank']

    def __unicode__(self):
        return self.name
