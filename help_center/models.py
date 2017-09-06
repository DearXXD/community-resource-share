# coding:utf-8
from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.

class Help_category(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=timezone.now)  # 创建时间

    def __unicode__(self):
        return self.name

    @classmethod
    def deleted_category(cls,pk_list):
        # for i in pk_list:
        try:
            cate = cls.objects.get(id = pk_list)
        except Help_category.DoesNotExist:
            return  {'status':0,'msg':'没有此类别'}
        try:
            ar_number = Help_article.objects.filter(category=cate)
        except Help_article.DoesNotExist:
            pass
        if not ar_number:
            try:
                cate.delete()
            except:
                return {'status': 0, 'msg': '删除失败'}
            return {'status': 1, 'msg': '删除ok'}
        else:
            return {'status':0,'msg':'请删除该类别所有文件，在尝试删除此类别'}

    @classmethod
    def create_category(cls,name):
        cate = cls.objects.create(name=name)
        cate.save()
        return cate.id

class Help_article(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    content = models.TextField()
    document = models.FileField(upload_to='help_center/article/%Y/%m/%d',blank=True,null=True)  # 文件地址
    document_name= models.CharField(max_length=50,default='document')
    category = models.ForeignKey(Help_category,related_name='+')
    create_time = models.DateTimeField(default=timezone.now)  # 创建时间

    def __unicode__(self):
        return self.title

    @classmethod
    def post_article(cls,title,content,category_id,user,document):
        try:
            category = Help_category.objects.get(id =category_id)
        except Help_category.DoesNotExist:
            return {'status':0,'msg':'清选择合适的分类'}
        if document != '':
            try:
                art = cls.objects.create(title = title,content = content,category=category,user=user,document=document,document_name=document.name)
                art.save()
            except:
                return {'status': 0, 'msg': '创建失败'}
            return {'status': 1, 'msg': '创建成功'}
        else:
            try:
                art = cls.objects.create(title=title, content=content, category=category, user=user)
                art.save()
            except:
                return {'status': 0, 'msg': '创建失败'}
            return {'status': 1, 'msg': '创建成功'}

    @classmethod
    def get_search(cls,title):
        '''搜索'''
        try:
            querryset = Help_article.objects.filter(title__contains = title )
        except:
            print 132
            return {'status':0,'msg':'没有你要找的文章'}
        if querryset:
            return {'status':1,'msg':'ok','querryset':querryset}
        else:
            return {'status': 0, 'msg': '没有你要找的文章'}

    @classmethod
    def get_article_list(cls):
        '''获取全部文章'''
        querry_set = Help_article.objects.all().order_by('-create_time')
        if not querry_set:
            return {'status':0,'msg':'没有你要找的文章'}
        return  {'status':1,'msg':'ok','querry_set':querry_set}

    @classmethod
    def get_category_article(cls,category_id):
        '''按类别获取数据'''
        try:
            category = Help_category.objects.get(id=category_id)
        except Help_category.DoesNotExist:
            return {'status': 0, 'msg': '清选择正确的分类'}
        try:
            querry_set = Help_article.objects.filter(category = category).order_by('-create_time')
        except:
            return {'status':0,'msg':'当前类别没有文章'}
        if  not querry_set:
            return {'status': 0, 'msg': '当前类别没有文章'}
        else:
            return {'status': 1, 'msg': 'ok', 'querry_set': querry_set}

    @classmethod
    def update_article(cls,pk,title,content,category_id,document):
        '''更新，编辑'''
        try:
            category = Help_category.objects.get(id =category_id)
        except Help_category.DoesNotExist:
            return ({'status':0,'msg':'清选择合适的分类'})
        try:
            article = cls.objects.get(id = pk)
        except Help_article.DoesNotExist:
            return {'status':0,'msg':'选择正确的文章'}
        article.title = title
        article.content = content
        article.category = category
        if document != '':
            article.document=document
            article.document_name = document.name
        article.save()
        return {'status': 1, 'msg': 'ok'}

    @classmethod
    def deleted_art(cls, pk_list):
        for i in pk_list:
            try:
                art = cls.objects.get(id=i)
            except Help_article.DoesNotExist:
                return {'status':0,'msg':'选择正确的文章'}
            art.delete()
            return  {'status':1,'msg':'删除成功'}
