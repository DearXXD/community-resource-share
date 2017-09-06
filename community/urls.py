# coding:utf-8
from django.conf.urls import include, url
from community.views import *

urlpatterns = [
    url(r'get-province/$', ProvinceViewSet.as_view({'get':'get_province'})),
    url(r'province/(?P<province_id>\d{1,11})/get-city/$', CityViewSet.as_view({'get':'get_city'})),  # 获取市，
    url(r'city/(?P<city_id>\d{1,11})/get-district/$', DistrictViewSet.as_view({'get':'get_district'})),  # 获取县，
    url(r'create/$', CommunityViewSet.as_view({'post': 'create'}), name='community-create'),  # 创建社区
    url(r'(?P<pk>\d{1,11})/modify/$', CommunityViewSet.as_view({'post': 'modify'}),name='community-modify'),  # 修改社区信息
    url(r'list/$', CommunityViewSet.as_view({'get': 'list'}), name='community-list'),  # 社区列表
    url(r'sort/$', CommunityViewSet.as_view({'post': 'sort_obj'}), name='community-sort'),  # 社区排序
    url(r'delete_list/$', CommunityViewSet.as_view({'post': 'delete_list'}), name='community-delete_list'),  # 删除社区列表
    url(r'search/$', CommunityViewSet.as_view({'post': 'search'}), name='community-search'),  # 搜索社区
    url(r'search_obj/$', CommunityViewSet.as_view({'post': 'search_obj'}), name='community-search_obj'),  # 搜索社区名字模糊
    url(r'(?P<pk>\d{1,11})/detail/$', CommunityViewSet.as_view({'get': 'detail'}), name='community-detail'),  # 获取社区详情
    url(r'join_community/$', CommunityViewSet.as_view({'get': 'join_community'}), name='community-join'),# 加入社区
    url(r'get_my_community_list/$', CommunityViewSet.as_view({'get': 'get_my_community_list'}),name='get_my_community_list'),  # 获得我的社区
    url(r'screen_community/$', CommunityViewSet.as_view({'get': 'screen_community'}),name='screen_community'),  # 筛选社区
    url(r'send/$', CommunityViewSet.as_view({'get': 'send'}),name='send'),  # 筛选社区
    url(r'save_file/$', CommunityViewSet.as_view({'post': 'save_file'}),name='save_file'),  # 筛选社区
]