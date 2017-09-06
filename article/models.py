# coding:utf8
from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from ckeditor.widgets import CKEditorWidget
from django.contrib.contenttypes import generic
from comments.models import Comment
from django.db.models.signals import pre_save

class ArticleCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'名字')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',verbose_name=u'上一级目录')

    class Meta:
        verbose_name = u'文章分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name=u'标题')
    author = models.ForeignKey(User, related_name="artilces",verbose_name=u'作者')   # 作者
    text = RichTextField(config_name='default',verbose_name=u'内容')
    is_top = models.BooleanField(verbose_name=u'是否置顶')    # 置顶
    category = models.ManyToManyField(ArticleCategory,verbose_name=u'文章类型')
    cover_img = models.ImageField(null=True, upload_to="article_cover", blank=True,verbose_name=u'图片')
    click_num = models.IntegerField(default=0,verbose_name=u'点击量')  # 点击量
    dateline = models.DateTimeField(default=timezone.now,verbose_name=u'日期')
    comments = generic.GenericRelation(Comment,verbose_name=u'评论')  # 评论

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
