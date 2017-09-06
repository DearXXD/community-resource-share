# coding:utf-8
from django.shortcuts import render
from help_center.models import *
from help_center.serializers import *
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, status
import json
from utils.test import  login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from accounts.permission import perm_require,back_perm_require
import math
# Create your views here.
class help_category(viewsets.ModelViewSet):
    queryset =  Help_category.objects.all()
    serializer_class = Help_categorySerializers

    @csrf_exempt
    # @back_perm_require()
    def POST_create(self, request):
        '''创建分类'''
        if request.method == 'POST':
            name = request.data.get('name',None)
            if name != None:
                a = Help_category.create_category(name)
                return Response({'status':1,'msg':'创建成功','id':a})
            else:
                return Response({'status':0,'msg':'post方式访问'})

    @csrf_exempt
    # @back_perm_require()
    def DELETE_category(self,request):
        '''删除分类'''
        if request.method == 'POST':
            pk_list = request.data.get('pk_list',None)
            if pk_list != None:
                cate = Help_category.deleted_category(pk_list)
            else:
                return Response({'status':1,'msg':'请选择合适的分类'})
            return Response(cate)

    @csrf_exempt
    def Get_category_list(self,request):
        '''获取分类'''
        queryset = Help_category.objects.all()
        l=[]
        for i in queryset:
            if i.name:
                l.append({'c_id':i.id,'c_name':i.name})
        return Response(l)


class help_article(viewsets.ModelViewSet):
    queryset = Help_article.objects.all()
    serializer_class = Help_articeSerializers

    # @login_required
    @csrf_exempt
    def GET_aaticle_as_pk(self,request):
        '''获取具体文章'''
        if request.method == 'POST':
            pk = request.data.get('pk',None)
            try:
                art = Help_article.objects.get(id = int(pk))
            except Help_article.DoesNotExist:
                return Response({'status':0,'msg':'选择合适的文章'})
            ser =   Help_articeSerializers(art).data
            return  Response(ser)

    @csrf_exempt
    def GET_search(self,request):
        '''搜索'''
        if request.method == 'POST':
            page = request.data.get('page',1)
            title = request.data.get('title',None)
            if title != None:
                article = Help_article.get_search(title)
                if article['status'] == 0:
                    return Response(article)
                elif article['status'] == 1:
                    count = article['querryset'].count()
                    serializers = Help_articeSerializers(article['querryset'],many=True).data
                    page_num = 10
                    start_p = int(int(int(page) - 1) * page_num)
                    end_p = int(int(page) * page_num)
                    page_number = math.ceil(float(count) / page_num)
                    if int(page) > int(page_number):
                        return Response({'status': 0, 'msg': '请选择合适的页码'})
                    l = []
                    for ser in serializers:
                        ser_d = dict(ser)
                        l.append(ser_d)
                    if l:
                        l[0]['page_number'] = page_number
                    con = l[start_p:end_p]
                    return Response(con)
                    # return Response(ser)
            else:
                return Response({'status': 0, 'msg': '请传入合适的名称'})

    @csrf_exempt
    def Get_article_list(self,request):
        '''获取文章列表'''
        page=request.data.get('page',1)
        article = Help_article.get_article_list()
        if article['status'] == 0:
            return Response(article)
        elif article['status'] == 1:
            count =  article['querry_set'].count()
            serializers = Help_articeSerializers(article['querry_set'],many=True).data
            page_num = 10
            start_p = int(int(int(page) - 1) * page_num)
            end_p = int(int(page) * page_num)
            page_number = math.ceil(float(count) / page_num)
            if int(page) > int(page_number):
                return Response({'status': 0, 'msg': '请选择合适的页码'})
            l = []
            for ser in serializers:
                ser_d = dict(ser)
                l.append(ser_d)
            if l:
                l[0]['page_number'] = page_number
            con = l[start_p:end_p]
            return Response(con)

    @csrf_exempt
    def Get_category_article(self,request):
        '''按分类获取文章'''
        if request.method == 'POST':
            page = request.data.get('page', 1)
            category_id = request.data.get('category_id',None)
            if category_id:
                article = Help_article.get_category_article(category_id)
                if article['status'] == 1:
                    a=article['querry_set']
                    count = article['querry_set'].count()
                    serializers = Help_articeSerializers(a,many=True).data
                    page_num = 10
                    start_p = int(int(int(page) - 1) * page_num)
                    end_p = int(int(page) * page_num)
                    page_number = math.ceil(float(count) / page_num)
                    if int(page) > int(page_number):
                        return Response({'status': 0, 'msg': '请选择合适的页码'})
                    l = []
                    for ser in serializers:
                        ser_d = dict(ser)
                        l.append(ser_d)
                    if l:
                        l[0]['page_number'] = page_number
                    con = l[start_p:end_p]
                    return Response(con)
                elif article['status'] == 0:
                    return Response(article)
            else:
                return Response({'status': 0, 'msg': '请选择合适类别'})

    @csrf_exempt
    # @back_perm_require()
    def POST_article(self,request):
        '''编辑文章'''
        if request.method == 'POST':
            pk = request.data.get('pk','')
            title = request.data.get('title',None)
            content = request.data.get('content',None)
            category_id= request.data.get('category_id',None)
            document = request.data.get('document', '')
            if pk == ''and content == '' and category_id=='':
                return Response({'status': 0, 'msg': '请填写完整'})
            if str(document) == 'undefined':
                document =''
            if pk != '' and title != None and content != None and category_id != None:
                art = Help_article.update_article(pk,title,content,category_id,document=document)
                return Response(art)
            elif  pk == '' and title != None and content != None and category_id != None:
                user = request.user
                Help_article.post_article(title, content, category_id, user, document)
                return Response({'status': 1, 'msg': 'ssuess'})
            else:
                return Response({'status': 0, 'msg': '请填写完整'})

    @csrf_exempt
    # @back_perm_require()
    def DELETE_art(self,request):
        '''删除文章'''
        if request.method == 'POST':
            pk_list = request.data.getlist('pk_list',None)
            if pk_list!='' and pk_list!=None:
                cate = Help_article.deleted_art(pk_list)
                return Response(cate)
            else:
                return Response({'status': 0, 'msg': '请选择删除文章'})






