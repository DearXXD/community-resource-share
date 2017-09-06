# encoding:utf-8
from django.shortcuts import render
from .models import Province,Community,City,District
from rest_framework import viewsets,serializers,status
from .serializers import CommunitySerializer,ProviceSerializer,CitySerializer,DistrictSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from accounts.models import User
from django.db.models import Q
from util.response import JsonResponse
from util.mixin import GenericMethodMixin,PageReponseMixin
from util.viewset import ViewSet
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from util.msg import s_message_t
import os,sys
from django.conf import settings
import random
from django.core.files.uploadedfile import UploadedFile
# Create your views here.

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProviceSerializer

    def get_province(self,request):
        '''获取省'''
        pro = Province.objects.all()
        serializer = ProviceSerializer(pro,many=True)
        return JsonResponse(serializer.data)

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_city(self,request, province_id):
        '''
        获取市
        :param request:
        :param province_id: 省id‘
        :return:
        '''
        citys = City.objects.filter(province_id=province_id)
        serializer =CitySerializer(citys,many=True)
        return JsonResponse(data=serializer.data)

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    model_class =Community

    def get_district(self,request, city_id):
        '''
        获取县
        :param request:
        :param city_id: 市id
        :return:
        '''
        districts = District.objects.filter(city_id=city_id)
        serializer = DistrictSerializer(districts,many=True)
        return JsonResponse(data=serializer.data)

class CommunityViewSet(viewsets.ModelViewSet,GenericMethodMixin,PageReponseMixin):
    queryset = Community.objects.all().order_by('-join_time')
    serializer_class = CommunitySerializer
    model_class= Community
    model = Community.objects
    # permission_classes = (IsAuthenticated,)

    def create(self,request,*args,**kwargs):
        user = request.user
        data = request.data
        serializer = CommunitySerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse(code=JsonResponse.CODE_ERROR_DATA, data=serializer.errors)
        serializer.save(manager=user)
        community = serializer.instance
        community.members.add(user)
        community.save()
        return JsonResponse(u'创建成功',status=1)

    # def modify(self, request, community_id):
    #     data = request.data
    #     try:
    #         community =  Community.objects.get(id=community_id)
    #     except Community.DoesNotExist:
    #         raise Http404(u'社区不存在')
    #     for key in data.keys():
    #         community.__setattr__(key, data[key])
    #         community.save()
    #     return JsonResponse(u'成功')

    def join_community(self, request, community_id):
        """
        加入社区
        :param request:
        :param community_id: 社区id
        :return:
        """
        user = request.user
        try:
            community = Community.objects.get(id=community_id)
        except Community.DoesNotExist:
            raise Http404(u'社区不存在')
        community.members.add(user)
        community.save()
        return JsonResponse(msg=u'加入成功',status=1)


    def get_my_community_list(self, request):
        """
        获取我的社区列表
        :param request:
        :return:
        """
        print 12312
        user = request.user

        queryset = Community.objects.filter(members=user)
        serializer = self.get_serializer(queryset,many=True)
        return Response({'data':serializer.data})
        page = self.paginate_queryset(queryset)
        return self.get_paginated_response_status(request, queryset,status=1)

    def screen_community(self,request):
        '''
        筛选社区
        :param request:
        :return:
        '''
        data = request.data
        status = data.get('status',None)
        province_id = data.get('province_id',None)
        city_id = data.get('city_id',None)
        district_id = data.get('district_id',None)
        if province_id  and not city_id  and not status  and not district_id :
            q = Q(province_id=province_id)
        elif province_id and city_id and not status and not district_id:
            q = Q(province_id=province_id)|Q(city_id=city_id)
        elif province_id and city_id and not status and  district_id:
            q = Q(province_id=province_id)|Q(city_id=city_id)|Q(district_id=district_id)
        elif province_id and city_id and  status and not district_id:
            q = Q(province_id=province_id) | Q(city_id=city_id) | Q(district_id=district_id)|Q(status= status)
        instances = self.model_class.objects.filter(q)
        ser = self.serializer_class(instances,many=True).data
        return Response({'status':1,'data':ser})


    def send(self,request):
        # s_message_t(['13438326909','13438811615','13540354036'], ['asjdhjkasbdnjk'])
        a = s_message_t(["13551832256"], ["ttfirm", "username"])
        print a
        return Response({'status':1,'data':132132})

    def mkdir(patha):
        # 去除左右两边的空格
        patha = patha.strip()
        # 去除尾部 \符号
        patha = patha.rstrip("\\")
        if not os.patha.exists(patha):
            os.makedirs(patha)
        return patha

    def get_file_extension(file):
        return os.path.splitext(file)[1]

    def save_file(self,request ):
        data = request.data.get('pic',None)
        patha = os.path.join(settings.MEDIA_ROOT,'media/test/')
        file_name = str(random.randint(1111,123456))+'.png'
        if data == None:
            return
        self.mkdir(patha)

        file = open(patha + file_name, "wb")
        file.write(data)
        file.flush()
        file.close()
        return  Response({'msg':'ok'})



