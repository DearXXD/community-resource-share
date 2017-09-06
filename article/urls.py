# coding:utf-8
from django.conf.urls import include, url
from article import views


urlpatterns = [
    url(r'^category/create/$', views.ArticleCategoryViewSet.as_view({'post':'create'})),  # 创建分类
    url(r'^category/list/$', views.ArticleCategoryViewSet.as_view({'get':'list'})),  # 分类列表
    url(r'^category/(?P<pk>\d{1,11})/detail/$', views.ArticleCategoryViewSet.as_view({'get':'category_detail'})),  # 分类详情

    url(r'^$', views.ArticleViewSet.as_view({'get':'list','post':'create'})),  # 文章列表
    url(r'^update/$', views.ArticleViewSet.as_view({'post':'update'})),  # 修改文章
    # url(r'^list/$', views.ArticleViewSet.as_view({'get':'list'})),  # 修改文章
    url(r'^(?P<pk>\d{1,11})/detail/$', views.ArticleViewSet.as_view({'get':'detail'}), name='article-detail'),  # 查看详情
    url(r'^(?P<pk>\d{1,11})/comment_art/$', views.ArticleViewSet.as_view({'post': 'comment'}), name='article-comment'),# 评论文章
    url(r'^(?P<pk>\d{1,11})/comment_list/$', views.ArticleViewSet.as_view({'get': 'comment_list'}), name='article-comment-list'),# 评论文章
]
