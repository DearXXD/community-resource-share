# encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,Group
from django.utils import timezone
from accounts.fields import ListField
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,username,password):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username)
        user.set_password(password)
        user.last_login=timezone.now()
        user.save(using=self._db)
        return  user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user



IS_ARCHIVE = (
    (1, '冻结'),
    (2, '正常'),
    (3, '删除'),
)
USER_TYPE = (
    (1, '用户'),
    (2, '社区管理员'),
    (3, '超级管理员'),
)

class User(AbstractBaseUser):
    username = models.CharField(max_length=30,unique=True,verbose_name=u'用户名')
    is_active = models.BooleanField(default=True,verbose_name=u'激活')
    is_staff = models.BooleanField( default=True,verbose_name=u'管理员f')
    is_admin = models.BooleanField(default=False, verbose_name=u'管理员')
    date_joined = models.DateTimeField(u"加入时间", default=timezone.now())
    email = models.EmailField(null=True, blank=True, unique=True)
    status = models.IntegerField(u'状态',choices=IS_ARCHIVE, default=2)
    group = models.ManyToManyField(Group,null=True, blank=True)  # 用户组
    real_name = models.CharField(max_length=30,default='ttname')
    objects = MyUserManager()
    address = models.CharField(max_length=40,blank=True,null=True,verbose_name=u'地址')
    id_card = models.CharField(u'身份证号', max_length=20, null=True, blank=True, unique=True)  # 身份证号
    # facade_id_card = models.ImageField(u'身份证正面',upload_to='user/idcard/%Y/%m/%d', null=True, blank=True)   # 身份证正面
    # obverse_id_card = models.ImageField(u'身份证反面',upload_to='user/idcard/%Y/%m/%d', null=True, blank=True)  # 身份证反面
    # living_proof= models.ImageField(u'居住证明',upload_to='user/living_proof/%Y/%m/%d', null=True, blank=True)
    join_time = models.DateTimeField(u'加入时间',default=timezone.now())
    type = models.IntegerField(u'类型',choices=USER_TYPE, default=1)
    integration = models.IntegerField(default=500, verbose_name=u'信用积分')
    cart = ListField(default=[],blank=True,null=True,verbose_name=u'购物车')

    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = u"用户"

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

    # 必须重写方法
    def get_full_name(self):
        return self.username

    # 必须重写方法
    def get_short_name(self):
        return self.username

    #判断权限
    def has_group_perm(self, perm):
        perm_qset = self.group.filter(permissions__name=perm)
        groups = self.group.all()
        for group in groups:
            permissions = group.permissions.all()
            for permission in permissions:
                if permission.name == perm:
                    return True

    def has_perms(self, perm, obj=None):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,*args,**kwargs):
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def get_community(self):
        """获得我的community"""
        community_set = self.community.all()
        if community_set.count() > 0:
            return community_set[0]
        else:
            return None