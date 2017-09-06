# coding:utf-8
from django.db import models
from django.utils import timezone
from accounts.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    text = models.TextField(verbose_name=u'内容')
    author = models.ForeignKey(User,verbose_name=u'作者')
    dateline = models.DateTimeField(default=timezone.now,verbose_name=u'日期')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.author.username

    def get_comments_by_user_id(self, user_id):
        """
        获取指定用户的评论
        :param user:
        :return:
        """
        comment_set = self.objects.filter(author__id=user_id).order_by('-dateline')
        return comment_set