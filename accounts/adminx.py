# coding:utf-8
import xadmin
from xadmin import views
from .models import User
from article.models import Article,ArticleCategory
from comments.models import Comment
from community.models import Province,City,District,Community,Community_Statistical
from order.models import Order
from resources.models import Resource,Category,Respic
from django.contrib.auth.models import Group, Permission

class BaseSetting(object):
    '''
    设置主题
    增加models添加选择
    '''
    enable_themes=True
    use_bootswatch=True
xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    '''
    设置头标题
    设置底标题
    设置每一个app的下拉菜单
    '''
    site_title=u"社区资源共享系统后台管理"
    site_footer=u"社区资源共享系统后台管理"
    menu_style="accordion"
    apps_label_title = {
        "accounts": u"用户",
        "community": u"社区管理",
        "comments": u"评论管理",
        "order": u"订单管理",
        "auth": u"组",
        "article": u"咨询通告",
        "resources": u"资源",
    }
xadmin.site.register(views.CommAdminView,GlobalSettings)

# xadmin.site.unregister(Group)
# xadmin.site.unregister(Permission)
xadmin.site.unregister(User)

class OrderAdmin(object):
    list_display = ['order_number', 'intergration' , 'master' , 'resource' , 'buyer' ,'community' ,'process']
    search_fields =  ['order_number','master']
    list_filter =  ['order_number', 'intergration' , 'master' , 'resource' , 'buyer' ,'community', 'is_complete' ,'is_damage','damage_pic' ,'process','begin_time','end_time']
xadmin.site.register(Order,OrderAdmin)

class UserAdmin(object):
    list_display = ["username",'email','id_card','status','type','join_time','integration',]
    search_fields = ["username"]
    list_filter =["username",'email','id_card','status','type','join_time','integration',]
xadmin.site.register(User, UserAdmin)

class ArticleAdmin(object):
    list_display = ['title', 'author',  'dateline']
    search_fields = ['title', 'author', 'category']
    list_filter = ['title', 'author', 'category', 'dateline']
xadmin.site.register(Article,ArticleAdmin)

class ArticleCategoryAdmin(object):
    list_display = ['name','parent']
    search_fields =  ['name','parent']
    list_filter =  ['name','parent']
xadmin.site.register(ArticleCategory,ArticleCategoryAdmin)

class CommentAdmin(object):
    list_display = ['author','dateline']
    search_fields =  ['author',]
    list_filter =   ['author','dateline']
xadmin.site.register(Comment,CommentAdmin)

# xadmin.site.register(Province)
# xadmin.site.register(City)
# xadmin.site.register(District)
xadmin.site.register(Community)
# xadmin.site.register(Community_Statistical)


xadmin.site.register(Category)

class ResourceAdmin(object):
    list_display = ['name','master','community']
    search_fields =  ['name','community']
    list_filter =   ['name','master','community']
xadmin.site.register(Resource,ResourceAdmin)


