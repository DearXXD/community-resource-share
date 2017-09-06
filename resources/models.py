# coding:utf-8
from django.db import models
from accounts.models import User
from community.models import Community
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.contenttypes import generic
from comments.models import Comment
from ckeditor.fields import RichTextField
from accounts.fields import ListField

class Category(models.Model):
    """类别"""
    name = models.CharField(max_length=30, verbose_name=u'类别')  # 类型名
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'创建时间')  # 创建时间
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='child_categories',
                               verbose_name=u'上一级目录')  # 父级分类
    layer = models.IntegerField(u'层级', default=0)  # 层级
    can_delete = models.BooleanField(default=True, verbose_name=u'是否可以删除')

    class Meta:
        verbose_name = u'资源分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """保存"""
        if self.parent:
            self.layer = self.parent.layer + 1
        super(Category, self).save(*args, **kwargs)

    def get_resource_num(self):
        return self.resources.count()

    def rename(self, name):
        """重命名"""
        self.name = name
        self.save()

    def get_resources(self):
        """
        获取资源列表
        :return:
        """
        return self.resources.all()

class Respic(models.Model):
    pic = models.ImageField(upload_to='resource_pic/%Y/%m/%d', verbose_name=u'物品照片')

class Resource(models.Model):
    # 物品描述
    description =RichTextField(verbose_name=u'物品描述')
    master = models.ForeignKey(User,verbose_name=u'物品所属人')
    community = models.ForeignKey(Community, verbose_name=u'物品所属社区',null=True, blank=True )
    resource_picture = models.ImageField(upload_to='resource_picture/%Y/%m/%d', verbose_name=u'物品照片',blank=True,null=True)
    name = models.CharField(max_length=30, verbose_name=u'物品名字')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name=u'发布日期')
    use_time = models.DateTimeField(default=(timezone.now()+timedelta(days=5)),verbose_name=u'使用期限', blank=True, null=True)
    return_time = models.DateTimeField(verbose_name=u'归还日期', null=True, blank=True ,default=None)
    intergration = models.IntegerField(default=None,blank=True,null=True,verbose_name=u'所需积分')
    is_active = models.BooleanField(default=True, verbose_name=u'激活状态')
    # pic = models.ManyToManyField(Respic,verbose_name=u'pics',related_name='resources',null=True, blank=True)
    pic = ListField(default=[])
    is_used = models.BooleanField(default=False, verbose_name=u'是否被使用')
    focus = models.ManyToManyField(User,related_name='focus',verbose_name=u'关注',null=True, blank=True)
    pub_address = models.CharField(u'发布地址',max_length=25)
    category = models.ManyToManyField(Category, verbose_name=u'类别',related_name='resources', null=True, blank=True)
    comments = generic.GenericRelation(Comment,verbose_name=u'评论',blank=True,null=True)  # 评论

    rate = models.CharField(max_length=10,blank=True,null=True,verbose_name=u'评分')
    rate_content = models.TextField(blank=True,null=True,verbose_name=u'评价内容')
    picList = ListField(blank=True,null=True,verbose_name=u'评价图片')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name






