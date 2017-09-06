# coding:utf-8
from django.db import models
from accounts.models import User
from community.models import Community
from django.utils import timezone
from resources.models import Resource
from datetime import datetime, timedelta

# Create your models here.
PROCESS=(
    (1,'锁定使用'),
    (2,'取消锁定'),
    (3,'使用中'),
    (4,'归还'),
    (5,'评价'),
)
class Order(models.Model):
    order_number = models.CharField(u'订单号',max_length=25,unique=True)
    intergration = models.IntegerField(u'积分')
    master = models.ForeignKey(User, related_name='master_order', verbose_name=u'物品所属人')
    resource = models.ForeignKey(Resource,related_name='order', verbose_name=u'资源')
    buyer = models.ForeignKey(User,related_name='buyer_order', verbose_name=u'使用者')
    community = models.ForeignKey(Community, verbose_name=u'订单所属社区')
    is_complete = models.BooleanField(u'交换是否后完成',default=False)
    is_damage = models.BooleanField(u'是否损坏',default=False)
    damage_pic = models.ImageField(u'损坏部分的照片',upload_to='order/damage/%Y/%m/%d',blank=True,null=True,default=None)
    process = models.IntegerField(u'进程',choices=PROCESS,default=1)
    begin_time = models.DateField(u'开始时间',default=timezone.now())
    end_time = models.DateField(u'完成时间',blank=True,null=True,default=None)

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.order_number

    # def save(self, *args, **kwargs):
    #     """保存"""
    #     # self.community = self.master.community()
    #     # self.intergration = self.resource.scores
    #
    #     super(Order, self).save(*args, **kwargs)
    #     if self.process == 3:
    #         self.buyer.credit_score = self.buyer.credit_score - self.intergration
    #     self.save()

    def transform_order_process(self):
        '''
        改变订单进程，向前推进一步
        :return: 成功  True
        '''
        if 0 < self.process < 3:
            self.process = self.process + 1
            return True
        else:
            return False

    def complete_order(self):
        '''
        完成订单
        :return:
        '''
        if 0 < self.process < 3:
            self.process = self.process + 1
            if self.process != 3 :
                return False
            self.end_time = timezone.now()
            return True
        else:
            return False

# class UseHistory(models.Model):
#     master = models.ForeignKey(User,related_name='master_his')
#     resource = models.ForeignKey(Resource,related_name='history')
#     use_time = models.CharField(max_length=20,verbose_name='使用时间')
#     order = models.OneToOneField(Order,related_name='history')
#     buyser = models.ForeignKey(User,null=True,default=None,blank=True,related_name='buyer_his')
#
#     def save(self,*args,**kwargs):
#         buyer = self.order.buyer
#         super(UseHistory,self).save(*args,**kwargs)
