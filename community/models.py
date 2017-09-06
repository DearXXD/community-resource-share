# coding:utf-8
from __future__ import absolute_import
from __future__ import division
from django.db.models import Sum
from django.db import models
from accounts.models import User
from django.utils import timezone
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Province(models.Model):
    name =  models.CharField(max_length=45)
    orderid = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = u'省份'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    name  = models.CharField(max_length=45)
    areacode = models.CharField(max_length=45,null=True, blank=True)

    class Meta:
        verbose_name = u'市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=45)
    post_code = models.CharField(max_length=45,null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'县'
        verbose_name_plural = verbose_name

TATUS = (
    (0,u'正常'),
    (1,u'冻结'),
    (2,u'删除'),
    (3,u'待审核'),
    (4,u'通过审核'),
    (5,u'拒绝审核'),
)
# Create your models here.
class Community(models.Model):
    province = models.ForeignKey(Province, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    district = models.ForeignKey(District, null=True, blank=True)
    name  = models.CharField(u'社区名',max_length=25,unique=True)
    address = models.CharField(u'地址',max_length=35)
    manager = models.ForeignKey(User,null=True,related_name='community', blank=True,verbose_name='管理员')
    members = models.ManyToManyField(User,verbose_name=u'成员',related_name='belong_to_community',null=True, blank=True) #成员
    status = models.IntegerField(u'状态',choices = TATUS,default=3)  #状态
    email = models.EmailField(u'邮箱',blank=True,null=True)  #邮箱
    phone = models.CharField(u'电话',max_length=11)  # 电话
    join_time = models.DateTimeField(u'加入时间',auto_now=True)
    seal = models.ImageField(u'公章',upload_to='community/seal/%Y/%m/%d', null=True, blank=True)  # 公章
    community_license_img = models.ImageField(u'相关证件描件',upload_to='community/license/%Y/%m/%d', null=True, blank=True)
    community_license = models.CharField(u'证件号',max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = u'社区'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def members_count(self):
        """
        成员数量
        :return:
        """
        return self.members.all().count()

    @classmethod
    def get_community_by_id(self,community_id):
        '''
        根据社区id获取社区
        :param community_id:
        :return:
        '''
        try:
            community = Community.objects.get(id=community_id)
            return community
        except Community.DoesNotExist:
            return None

    def get_member_set(self,**kwargs):
        '''
        获取社区成员
        :param kwargs:筛选条件
        :return:
        '''
        if kwargs:
            return self.members_set.filter(**kwargs)
        else:
            return self.members_set.all()

    def get_user_member_list(self,**kwargs):
        """
        获取社区内成员，用户对象列表
        :param kwargs:
        :return:
        """
        member_set = self.get_member_set(**kwargs)
        member_user_list = []
        for member in member_set:
            member_user_list.append(member.user)
        return member_user_list


    def _get_full_address(self):
        '''
        获取完整地址
        :return:
        '''
        return '%s%s%s' % (self.province.name,self.city.name,self.district.name)

    full_adress = property(_get_full_address)  #设置成属性







class Community_Statistical(models.Model):
    time = models.DateTimeField(default=timezone.now())  #创建时间
    community = models.ForeignKey(Community)        #名称
    is_added = models.IntegerField(default=0)       #是否增加,增加=1，没有增加=0
    is_deleted = models.IntegerField(default=0)     #是否删除 删除=1，没有删除=0
    member = models.IntegerField(default=0)         #user数量增加=1
    province = models.ForeignKey(Province)          #省份

    class Meta:
        verbose_name = u'社区统计'
        verbose_name_plural = verbose_name






