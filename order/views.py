# coding:utf-8
from order.models import Order
from util.response import JsonResponse,get_obj
from util.mixin import GenericMethodMixin,PageReponseMixin
from util.viewset import ViewSet
from order.serializers import OrderSerializer,OrderWithAllSerializer
import datetime
import random
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from resources.models import Resource

class OrderViewSet(ViewSet):
    queryset = Order.objects.all().order_by('-begin_time')
    serializer_class = OrderSerializer
    model_class =Order
    # permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        '''
        生成订单
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        buyer = request.user
        data_list = request.data.get('data',None)
        if  not data_list:
            return JsonResponse(u'请传入合适的参数',status = 0)
        for i in data_list:
            print i['id']
            if int(i['id']) not in buyer.cart:
                # return JsonResponse(u'参数错误',status=0)
                pass
        for data in data_list:
            master_id = data['master']['id']
            community_id = data['community']['id']
            resource_id = data['id']
            num = random.randint(1000000,9999999)
            serializer = self.serializer_class(data = data)
            try:
                res = Resource.objects.get(id = resource_id)
            except Resource.DoesNotExist:
                return JsonResponse('请选择合适的资源')
            if res.is_used:
                return JsonResponse('请选择合适的资源,资源正在被其他人使用')
            if not serializer.is_valid():
                return JsonResponse(JsonResponse.CODE_ERROR_DATA,serializer.errors)
            serializer.save(buyer=buyer,master_id = master_id,community_id = community_id,resource_id=resource_id,order_number=num)
            try:
                buyer.cart.remove(int(resource_id))
            except ValueError:
                # return JsonResponse(u'此资源还没有加入购物车',status=0)
                pass
            try:
                res=Resource.objects.get(id=resource_id)
                buyer.focus.remove(res)
            except ValueError:
                # return JsonResponse(u'此资源还没有加入购物车',status=0)
                pass
            buyer.save()
            res.is_used = True
            res.save()
        return JsonResponse('ok',status=1)

    def search_order_num(self,request):
        '''
        按订单号搜索，模糊匹配
        :param request: 搜索条件
        :return: 搜索结果
        '''
        search_content = request.data.get('s', None)
        if not search_content:
            return JsonResponse(msg='数据错误，缺少参数', code=502, status=0)
        instances = self.model_class.objects(order_number__contains=search_content)
        serializer = self.get_serializer(instances, many=True)
        return JsonResponse(msg='ok', data=serializer.data, status=1)

    def order_operation(self,request):
        '''
        订单操作，取消订单，锁定，使用，归还
        :param request:
        :return:
        '''
        data = request.data
        id = data.get('order_id',None)
        process_type = data.get('process',None)
        if not process_type and not id:
            return JsonResponse(JsonResponse.CODE_ERROR_DATA,status=0)
        order = get_obj(self.model_class,id)
        order.process = process_type
        if process_type == '4':     #归还
            order.end_time = datetime.datetime.now()
        elif process_type == '2':
            order.resource.is_used = False
        elif process_type == '3':   #使用
            order.buyer.intergration = order.buyer.intergration - order.intergration    #使用 用户积分扣除
            order.master.intergration = order.master.intergration + order.intergration  #发布 用户积分增加
        order.save()
        return JsonResponse('ok',status=1)

    def return_back(self,request):
        '''
        归还
        :param request:
        :return:
        '''
        order_id = request.data.get('order_id',None)
        order =  get_obj(self.model_class,order_id)
        if order.process in [1,2]:
            return JsonResponse(u'资源没有在使用中，请检查', status=0)
        order.process = 4
        order.save()
        return JsonResponse('ok',status=1)

    def cancel(self,request):
        '''
        取消
        :param request:
        :return:
        '''
        order_id = request.data.get('order_id',None)
        order =  get_obj(self.model_class,order_id)
        if order.process != 1:
            return JsonResponse(u'资源在使用中获取已关闭，请检查', status=0)
        order.process = 2
        order.resource.is_used = False
        order.resource.save()
        order.save()
        return JsonResponse('ok',status=1)

class OrderWithAllViewSet(ViewSet):
    queryset = Order.objects.all().order_by('-begin_time')
    serializer_class = OrderWithAllSerializer
    model_class = Order
    permission_classes = (IsAuthenticated,)
    def get_my_orders(self,request):
        user = request.user
        orders =  Order.objects.filter(buyer=user)
        serializer = self.serializer_class(orders,many=True)
        return self.get_paginated_response_status(request,orders)