# coding: utf-8
from django.db import models
from accounts.models import User
from django.utils import timezone

STATUS = (
    (1,'待审核'),
    (2,'通过'),
    (3,'拒绝'),
)


class Type(models.Model):
    type = models.CharField(u'类型',max_length=20)

class User_Response(models.Model):
    user_response = models.TextField(verbose_name='反馈')
    reply = models.ForeignKey('self',related_name='reply')#社区回复
    layer = models.IntegerField(u'层级',default=0)
    reply_community = models.ForeignKey('community.Community',blank = True,null=True,default=None)   #回复的社区

class Subscribe(models.Model):
    community = models.ForeignKey('community.Community')
    user = models.ForeignKey('accounts.User')
    subscribe_time = models.DateField(verbose_name=u'预约时间', default=timezone.now())
    type = models.ForeignKey(Type)
    content = models.TextField(u'预约内容')
    status = models.IntegerField(u'状态',choices=STATUS,default=1)
    refuse_reason = models.TextField(u'拒绝理由')
    is_deal = models.BooleanField(u'是否处理',default=False)
    response = models.ForeignKey(User_Response,related_name='+',blank = True,null=True,default=None,verbose_name=u'反馈')
    create_time = models.DateTimeField(default=timezone.now())


    class Meta:
        verbose_name = u'预约'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type.type









