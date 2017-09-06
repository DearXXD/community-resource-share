# coding:utf-8
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Resource,Category,Respic
from .serializers import ResourceSerializer,ResourceWithoutUserSerializer,CategorySerializer,CategoryWithoutParentSerializer,RespicSerializer
from util.viewset import ViewSet
from util.mixin import GenericMethodMixin,CommentMixin
from rest_framework.permissions import IsAuthenticated
from util.response import JsonResponse,get_obj
from django.http import Http404
from util.permission import is_login_require
from django.conf import settings
from order.models import Order
from django.db.models import Q
from django.core.files.uploadedfile import UploadedFile
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from django.conf import settings

# 平均哈希算法计算
def classify_aHash(image1, image2):
    image1 = cv2.resize(image1, (8, 8),interpolation = cv2.INTER_AREA)
    image2 = cv2.resize(image2, (8, 8),interpolation = cv2.INTER_AREA)
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hash1 = getHash(gray1)
    hash2 = getHash(gray2)
    return Hamming_distance(hash1, hash2)

# 输入灰度图，返回hash
def getHash(image):
    avreage = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash


# 计算汉明距离
def Hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


class ResourceViewSet(ViewSet,GenericMethodMixin,CommentMixin):
    '''
    获取资源的信息用于发布
    '''
    queryset = Resource.objects.all().order_by('-create_time')
    serializer_class = ResourceSerializer
    model_class =Resource
    # permission_classes = (IsAuthenticated,)

    def get_detail(self,request,pk):
        try:
            res = self.model_class.objects.get(id=pk)
        except self.model_class.DoesNotExist:
            return JsonResponse(u'请选择合适的资源',status=0)
        ser = self.get_serializer(res).data
        ser_dic = dict(ser)

        resource_picture =  '/media/' + str(res.resource_picture)
        if res.category.first():
            ser_dic[u'category'] = res.category.first().id
            ser_dic[u'resource_pictures'] = resource_picture

        if ser_dic['picList']:
            l_pic= []
            for pic in ser_dic['picList']:
                # pic = 'http://139.199.9.72:8010' + str(pic)
                pic = 'http://127.0.0.1:8000' + str(pic)
                l_pic.append(pic)
            ser_dic['picList'] = l_pic
        # pic_d={}
        # ser_dic[u'picList'] = []
        # for pic in res.pic:
        #     pic_d[u'name']='1.jpg'
        #     pic_d[u'url']=pic
        #     ser_dic[u'picList'].append(pic_d)
        # ser_dic[u'resource_picture']=[{u'name':'',u'url':str(res.resource_picture)}]
        return JsonResponse('ok',status=1,data = ser_dic)

    def create(self,request,pk=None):
        '''
        创建资源
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        import  urllib
        data = request.data
        user = request.user
        # print data
        category_id = data.pop('category',[])
        resource_pictures = data.pop('resource_picture',[])
        print resource_pictures

        resource_pictures=urllib.unquote_plus(resource_pictures)
        print resource_pictures
        fname = str(resource_pictures).split('/')[-1]
        file_size = os.path.getsize(settings.MEDIA_ROOT + resource_pictures.split('/media')[-1])
        with open(settings.MEDIA_ROOT + resource_pictures.split('/media')[-1],'r') as f:
            resource_picture =UploadedFile(f,name=fname,size=file_size)
            data['resource_picture']=resource_picture
            if not pk:
                serializer = self.get_serializer(data=data)
                if not serializer.is_valid():
                    return JsonResponse(code = JsonResponse.CODE_ERROR_DATA,data =serializer.errors)
            else:
                try:
                    res = self.model_class.objects.get(id=pk)
                except self.model_class.DoesNotExist:
                    return JsonResponse(u'请选择合适的资源', status=0)
                resource_picture=data.get('resource_picture',None)
                if not resource_picture:
                    data.pop('resource_picture')
                serializer = self.get_serializer(instance=res,data=data)
                if not serializer.is_valid():
                    return JsonResponse(code=JsonResponse.CODE_ERROR_DATA, data=serializer.errors)
            community = user.belong_to_community.first()
            print 'com',community
            serializer.save(master=user,community_id=community.id)
            resource = serializer.instance
            # resource.community=community
            category = get_obj(Category,category_id)
            resource.category.add(category)
            resource.save()
        return JsonResponse(u'成功',status=1)


    @is_login_require()
    def focus(self,request,pk):
        '''
        关注资源
        :param request:
        :return:
        '''
        user = request.user
        obj = get_obj(self.model_class,pk)
        obj.focus.add(user)
        obj.save()
        return JsonResponse(u'关注成功',status=1)

    def list(self,request):
        # res = Resource.objects.filter(is_used=False)
        res = Resource.objects.filter(is_used=False)
        ser = self.get_serializer(res,many=True).data
        return JsonResponse(status=1,data = ser)

    def cancle_foc(self,request,pk):
        '''
        关注资源
        :param request:
        :return:
        '''
        user = request.user
        obj = get_obj(self.model_class,pk)
        obj.focus.remove(user)
        obj.save()
        return JsonResponse(u'关注成功',status=1)

    def get_top_ten(self):
        queryset = self.model_class.objects.filter(is_used=False).order_by('-create_time')[0:10]
        data = self.get_serializer(queryset,many=True).data
        return JsonResponse('ok',data=data,status=1)

    def get_leasted_5(self,request):
        queryset = self.model_class.objects.filter(is_used=False)[0:4]
        data = self.get_serializer(queryset,many=True).data
        return JsonResponse('ok',data=data,status=1)

    def get_foucs_num(self,request):
        queryset = self.queryset.first()
        a=queryset.focus.count()
        return JsonResponse('ok')

    def get_resource_category(self,request,pkc):
        category = get_obj(Category,pkc)
        if isinstance(category,Category):
            res = self.model_class.objects.filter(Q(category=category),Q(is_used=False))
            ser = self.get_serializer(res,many=True).data
            return JsonResponse('ok',status=1,data=ser)
        else:
            return JsonResponse(status=0)

    def get_collections(self,request):
        '''
        获取用户收藏资源
        :param request:
        :return:
        '''
        collections = request.user.focus.all()
        ser = self.get_serializer(collections,many=True).data
        return JsonResponse('ok',status = 1,data=ser)

    def get_pub(self,request):
        '''
        获取用户收藏资源
        :param request:
        :return:
        '''
        pubs = self.model_class.objects.filter(master=request.user)
        ser = self.get_serializer(pubs,many=True).data
        ser_ls= list(ser)
        l = []
        for pub in pubs:
            if pub.order.first():
                l.append(pub.order.first().process)
            else:
                l.append(0)

        for i in range(len(ser_ls)):
            if l:
                ser_ls[i]['process'] = l[i]
            if ser_ls[i]['picList']:
                l_pic= []
                for pic in ser_ls[i]['picList']:
                    # pic = 'http://139.199.9.72:8010' + str(pic)
                    pic = 'http://127.0.0.1:8000' + str(pic)
                    l_pic.append(pic)
                ser_ls[i]['picList'] = l_pic

        return JsonResponse('ok',status = 1,data=ser_ls)

    def rate_res(self,request):
        '''
        资源评价
        :param request:
        :return:
        '''
        data = request.data
        picList = data.get('picList',[])
        rate_content = data.get('rate_content',None)
        rate = data.get('rate',None)
        res_id = data.get('res_id',None)
        print picList
        try:
            res = Resource.objects.get(id=res_id)
        except Resource.DoesNotExist:
            return JsonResponse('请选择合适的资源',status=0)
        if rate and rate_content:
            res.rate = str(rate)
            res.rate_content = rate_content
            if picList:
                res.picList = picList
            res.save()
            orders = res.order.all()
            for order in orders:
                order.process = 5
                order.save()
        else:
            return JsonResponse('请填写合适的内容',status=0)
        return JsonResponse('ok',status=1)

    def find(self,request):
        fileList = request.data.get('fileList',None)
        n_path = settings.MEDIA_ROOT+str(fileList.split('media')[-1])
        print n_path
        resources = Resource.objects.filter(is_used=False)
        img1 = cv2.imread(n_path)
        l = []
        for res in resources:
            sou_path =os.path.join(settings.MEDIA_ROOT,str(res.resource_picture))
            print sou_path
            img2 = cv2.imread(sou_path)
            degree = classify_aHash(img1, img2)
            if degree <= 22:
                l.append(self.get_serializer(res).data)
            print degree
        return JsonResponse('ok',status=1,data=l)

class CategoryViewSet(ViewSet,GenericMethodMixin):
    queryset = Category.objects.all().order_by('-create_time')
    model_class =Category
    serializer_class = CategorySerializer


class PicViewSet(ViewSet,GenericMethodMixin):
    queryset = Respic.objects.all()
    model_class =Respic
    serializer_class = RespicSerializer

    def createp(self,request):
        pic = request.data.get('file',None)
        filename = request.data.get('filename',None)
        try:
            resp = Respic.objects.create(pic=pic)
        except:
            return JsonResponse('faile',status=0)
        print  'media/'+str(resp.pic)
        data = {'name':filename,'url':'/media/'+str(resp.pic)}
        return Response(data)






























