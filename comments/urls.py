# coding:utf-8
from django.conf.urls import include, url
from comments.views import CommentViewSet


urlpatterns = [
    url(r'comment/(?P<pk>\d{1,11})/$', CommentViewSet.as_view({'post':'comment'})),
    url(r'^(?P<pk>\d{1,11})/get_comment_comments/$', CommentViewSet.as_view({'get': 'get_comment_comments'}),name='comment-comment-list'),  # 评论文章

]