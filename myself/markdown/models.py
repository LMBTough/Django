from django.db import models
from django.conf import settings
import os
import datetime


# Create your models here.
class Mindnode(models.Model):
    name = models.CharField(max_length=30)
    path = models.FileField(upload_to='upload/')
    check_day = models.DateField(u'检查日期', auto_now=True)
    class Meta:
        db_table = 'Mindnode'
        verbose_name = 'Mindnode'
        verbose_name_plural = verbose_name
        ordering = ['check_day']


class Markdown(models.Model):
    name = models.CharField(max_length=30)
    path = models.FileField(upload_to='md/')
    belong = models.ForeignKey(Mindnode, null=True, blank=True)
    check_day = models.DateField(u'检查日期', auto_now=True)
    class Meta:
        db_table = 'Markdown'
        verbose_name = 'Markdown'
        verbose_name_plural = verbose_name
        ordering = ['check_day']
