# coding: utf-8
from django.db import models
from django.utils import timezone

class Certification(models.Model):
    community = models.ForeignKey('community.Community')
    description = models.TextField(verbose_name=u'流程描述', null=True, blank=True)
    qualification = models.ImageField(upload_to='办公/qualification/%Y/%m/%d', verbose_name=u'证书', null=True, blank=True)
    certify = models.ImageField(upload_to='办公/certify/%Y/%m/%d', verbose_name=u'证明', null=True, blank=True)
    create_time  =  models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'证明'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.description



























