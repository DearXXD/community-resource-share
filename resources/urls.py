# coding:utf-8
from django.conf.urls import include, url
from resources.views import ResourceViewSet,CategoryViewSet,PicViewSet

urlpatterns = [
    url(r'pic/create/$', PicViewSet.as_view({'post': 'createp'}), name='pic-create'),  # 删除资源分类列表
    url(r'create/$', ResourceViewSet.as_view({'post': 'create'}), name='resource-create'),  # 创建资源
    url(r'create/(?P<pk>\d{1,11})/$', ResourceViewSet.as_view({'post': 'create'}), name='resource-create'),  # 创建资源
    url(r'(?P<id>\d{1,11})/modify/$', ResourceViewSet.as_view({'post': 'modify'}),name='resource-modify'),  # 修改资源信息
    url(r'list/$', ResourceViewSet.as_view({'get': 'list'}), name='resource-list'),  # 资源列表
    url(r'search/$', ResourceViewSet.as_view({'post': 'search_obj'}), name='resource-search'),  # 搜索资源
    url(r'(?P<pk>\d{1,11})/detail/$', ResourceViewSet.as_view({'get': 'detail'}), name='resource-detail'),  # 获取资源详情
    url(r'(?P<pk>\d{1,11})/get_detail/$', ResourceViewSet.as_view({'get': 'get_detail'}), name='resource-get-detail'),  # 获取资源详情
    url(r'sort/$', ResourceViewSet.as_view({'post': 'sort_obj'}), name='resource-sort'),  # 资源排序
    url(r'delete/$', ResourceViewSet.as_view({'post': 'delete_list'}), name='resource-delete-list'),  # 删除资源列表
    url(r'search_obj/$', ResourceViewSet.as_view({'post': 'search_obj'}), name='resource-search-obj'),                                     # 搜索资源名字模糊
    url(r'(?P<pk>\d{1,11})/modify/$', ResourceViewSet.as_view({'post': 'modify'}), name='resource-modify'),                                # 修改资源信息
    url(r'(?P<pk>\d{1,11})/focus/$', ResourceViewSet.as_view({'post': 'focus'}), name='resource-focus'),                                   # 关注资源
    url(r'(?P<pk>\d{1,11})/cancle_foc/$', ResourceViewSet.as_view({'post': 'cancle_foc'}), name='resource-cancle-foc'),                    # 取消关注资源信息
    url(r'get_leasted_5/$', ResourceViewSet.as_view({'get': 'get_leasted_5'}), name='get-leasted-5'),                                      # 获取最新5资源信息
    url(r'get_top_ten/$', ResourceViewSet.as_view({'get': 'get_top_ten'}), name='get-top-ten'),                                            # 获取前10资源信息
    url(r'get_foucs_num/$', ResourceViewSet.as_view({'get': 'get_foucs_num'}), name='get-get_foucs_num-ten'),                              # 关注资源数
    url(r'(?P<pkc>\d{1,11})/get_resource_category/$', ResourceViewSet.as_view({'get': 'get_resource_category'}),name='get-res-cate-ten'),  # 根据类别获取资源

    url(r'comment_list/(?P<pk>\d{1,11})/$', ResourceViewSet.as_view({'get': 'comment_list'}),name='get-comment-list'),  # 评论列表
    url(r'comment/(?P<pk>\d{1,11})/$', ResourceViewSet.as_view({'post': 'comment'}),name='comment'),                    # 评论
    url(r'get_collections/$', ResourceViewSet.as_view({'get': 'get_collections'}),name='get_collections'),
    url(r'get_pub/$', ResourceViewSet.as_view({'get': 'get_pub'}),name='get_pubs'),
    url(r'rate_res/$', ResourceViewSet.as_view({'post': 'rate_res'}),name='rate-res'),
    url(r'find/$', ResourceViewSet.as_view({'post': 'find'}),name='find-res'),

    url(r'list_category/$', CategoryViewSet.as_view({'get': 'list'}), name='category-list'),  # 资源分类列表
    url(r'create_category/$', CategoryViewSet.as_view({'post': 'create'}), name='category-create'),  # 创建资源分类
    url(r'delete_list_category/$', CategoryViewSet.as_view({'post': 'delete_list'}), name='category-delete-list'),  # 删除资源分类列表
    url(r'delete_list_category/$', CategoryViewSet.as_view({'post': 'delete_list'}), name='category-delete-list'),  # 删除资源分类列表


]