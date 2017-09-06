# coding:utf-8
from django.conf.urls import include, url
from order.views import OrderViewSet,OrderWithAllViewSet

urlpatterns = [
    url(r'create/$', OrderViewSet.as_view({'post': 'create'}), name='order-create'),                                # 创建订单
    url(r'(?P<pk>\d{1,11})/modify/$', OrderViewSet.as_view({'post': 'modify'}),name='order-modify'),                # 修改订单信息
    url(r'list/$', OrderViewSet.as_view({'get': 'list'}), name='order-list'),                                       # 订单列表
    url(r'search/$', OrderViewSet.as_view({'post': 'search'}), name='order-search'),                                # 搜索订单
    url(r'(?P<pk>\d{1,11})/detail/$', OrderViewSet.as_view({'get': 'detail'}), name='order-detail'),                # 获取订单详情
    url(r'sort/$', OrderViewSet.as_view({'post': 'sort_obj'}), name='order-sort'),                                  # 订单排序
    url(r'delete/$', OrderViewSet.as_view({'post': 'delete_list'}), name='order-delete-list'),                      # 删除订单列表
    url(r'search_order_num/$', OrderViewSet.as_view({'post': 'search_order_num'}), name='order-number-search'),     # 按订单号搜索
    url(r'order_operation/$', OrderViewSet.as_view({'post': 'order_operation'}), name='order-operation'),           # 订单操作，取消订单，锁定，使用，归还
    url(r'get_my_orders/$', OrderWithAllViewSet.as_view({'get': 'get_my_orders'}), name='get-my-orders'),           # 获取我的订单
    url(r'return_back/$', OrderViewSet.as_view({'post': 'return_back'}), name='return-back'),                 # 归还
    url(r'cancel/$', OrderViewSet.as_view({'post': 'cancel'}), name='cancel'),                                # 取消订单
]