# encoding:utf-8
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=22,verbose_name=u'v称呼')
    email = models.EmailField(verbose_name=u'邮箱')
    content = models.TextField(verbose_name=u'意见反馈')
    is_replay = models.TextField(verbose_name=u'是否回访')
    remind = models.TextField(verbose_name=u'处理记录')
