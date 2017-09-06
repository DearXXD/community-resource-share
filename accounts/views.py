# encoding:utf-8
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from rest_framework.response import Response
from .serializers import UserSerializer,UserSerializerR
from rest_framework import routers, serializers, viewsets, status
from django.contrib import  auth
from util.message import *
from util.send_email import setEmail
from django.contrib.auth.models import Group
from community.models import Community
from util.response import JsonResponse,get_obj
from util.mixin import GenericMethodMixin,PageReponseMixin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from resources.models import Resource
from resources.serializers import ResourceSerializer
from ce.tasks import send_email_tt

def read_from_cache(request):
    keyy = "test"
    content = 'if you has hasjkdf '
    cache.set(keyy,content,timeout=0)
    a = cache.keys("t*")
    cache.ttl("foo")

def tes(request,u,p):
    user = authenticate(username=u,password=p)
    login(request,user)
    user =  request.user


def login_html(request):
    return render(request,'dist/index.html')

class UserVewSet(viewsets.ModelViewSet,GenericMethodMixin,PageReponseMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerR
    # permission_classes = (IsAuthenticated,)
    def get_user_info(self, request):
        obj = request.user

        serializer = self.serializer_class(obj, context={'request': request}).data
        community = request.user.belong_to_community.all()
        if community:
            serializer['region']=community[0].id
        else:
            serializer['region'] = ""
        return JsonResponse(data=serializer,status=1)

    def updata_user(self,request):
        data = request.data
        user = request.user
        address = data.get('address',None)
        email = data.get('email',None)
        real_name = data.get('real_name',None)
        id_card = data.get('id_card',None)
        region = data.get('region',None)

        user.address=address
        user.email=email
        user.real_name=real_name
        user.id_card=id_card
        user.save()
        user.belong_to_community.clear()
        user.save()
        com = Community.objects.get(id = int(region))
        com.members.add(user)
        com.save()
        return JsonResponse('ok',status=1)

    def get_username(self,request):
        user = request.user
        a = cache.get(str(user.username))
        print a
        if user.is_anonymous():
            return JsonResponse('error', status=0)
        name = request.user.real_name
        serializer = self.get_serializer(user).data
        focus = user.focus.all()
        res = ResourceSerializer(focus,many=True,context={'request': request}).data
        return JsonResponse(name,status=1,data=res)

    def remove_cart(self,request):
        '''
        删除出购物车
        :param request:
        :return:
        '''
        user = request.user
        data = request.data
        resource_list = data.get('res_list')
        print resource_list
        cart = user.cart
        for resource_id in resource_list:
            try:
                cart.remove(int(resource_id))
            except ValueError:
                pass
        user.save()
        return JsonResponse('ok',status=1)


    def add_cart(self,request,resource_id):
        '''
        加入购物车
        :param request:
        :return:
        '''
        user = request.user
        cart = user.cart
        is_collect = request.query_params.get('is_collect',None)
        try:
            res = Resource.objects.get(id=resource_id)
        except Resource.DoesNotExist:
            return JsonResponse('没有这个资源',status = 0)
        if int(resource_id) in cart:
            return JsonResponse('物品已在购物车',status=0)
        user.cart.append(int(resource_id))
        user.save()
        if is_collect == '1':
            user.focus.remove(res)
            user.save()
            collections = user.focus.all()
            ser = ResourceSerializer(collections, many=True,context={'request': request}).data
            return JsonResponse('ok', status=1, data=ser)
        return JsonResponse('ok',status=1)

    def get_cart_list(self,request):
        '''
        获取购物车列表
        :param request:
        :return:
        '''
        car_list = request.user.cart
        resources = Resource.objects.filter(id__in = car_list)
        serializer = ResourceSerializer(resources,many=True,context={'request': request})
        return JsonResponse('ok',data=serializer.data,status=1)



    @csrf_exempt
    def user_login(self,request):
        '''
        :param request:
        :return:
        '''
        data = request.data
        username = data.get('username',None)
        passwd = data.get('password',None)
        user = auth.authenticate(username=username,password=passwd)
        if not user:
            return JsonResponse(data={'status':0,'msg':'颤抖吧,凡人,你的用户名或者密码错误，哈哈哈'},status=0)
        if user.status == 3:
            return JsonResponse(data={'status':0,'msg':'你已经被删除,say goodbye~~'},status=0)
        elif user.status == 1:
            return JsonResponse(data={'status': 0, 'msg': '你已经被冻结,不能登录,请联系管理员,尽快承认错误'},status=0)
        auth.login(request, user)
        cache.set(str(user.username), user.real_name, timeout=300)
        return JsonResponse(data={'status': 1, 'msg': '被选召的孩子,出发吧','username':user.username},status=1)

    def user_logout(self,request):
        if request.user.is_anonymous():
            return JsonResponse(data={'msg':'faile','status':0},status=0)
        logout(request)
        return JsonResponse(data={'mag':'ok'},status=1)

    def regist(self,request,community_id):
        '''
        注册
        :param request:
        :param community:
        :return:
        '''
        data = request.data
        passwd = data.get('password',None)
        id_card = data.get('id_card',None)
        email = data.get('email',None)
        username = data.get('username',None)
        q = Q(Q(username=username)|Q(id_card=id_card)|Q(email=email))
        queryset = User.objects.filter(q)
        if queryset:
            return JsonResponse(data={'status':0,'msg':'您的账号被已注册'},status=0)
        try:
            user = User.objects.create(username=username,address = data.get('address',None),email=email,id_card=data.get('id_card',None))
        except:
            return JsonResponse(data={'status':0,'msg':'注册失败'},status=0)
        user.set_password(passwd)
        user.save()

        down = send_email_tt.s(user)
        down.delay()

        community = get_obj(Community,community_id)
        community.members.add(user)
        return JsonResponse(data={'status':1,'msg':'注册成功'},status=1)

    def get_model_obj(self,username):
        '''
        根据username获取对象
        :param username:
        :return:
        '''
        try:
            obj = self.model_class.objects.get(username=username)
        except self.model_class.DoesNotExist:
            obj = None
        return  obj

    def update_user(self,request):
        '''
        修改自己的个人信息
        :param request:
        :return:
        '''
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        if not serializer.is_valid():
            return Response({'status': 0, 'error': serializer.errors})
        serializer.save()
        return Response({'status': 1, 'msg': '更新成功'})

    #发送邮件
    def send_mail(request):
        data = request.data
        to = data.get('to', None)
        to = to.strip()
        try:
            user = User.objects.get(email=to)
        except User.DoesNotExist:
            return Response({'status': 0, 'msg': '这个邮箱不是用户'})
        if to:
            code = get_code()
            subject = '社区助手'
            form_email = '13540354036@163.com'
            html_content = '【社区助手】社区助手,您的验证码%s' % code
            setEmail(subject, form_email, to, html_content)
            print code
            cache.set(user.username,code,timeout=300)
            return Response({'status': 1, 'msg': u'发送成功,%s' % (code,)})
        else:
            return Response({'status': 0, 'msg': u'号码不正确，请重新填写'})

    # w忘记密码
    def forget_pwd(self, request):
        data = request.data
        username = data.get('username', None)
        new_passwd = data.get('new_passwd', None)
        re_new_passwd = data.get('re_new_passwd', None)
        ver = data.get('ver', None)
        if re_new_passwd != new_passwd:
            return Response({'status': 0, 'msg': '两次密码不相等,朋友~智商是个好东西,希望你也能拥有...'})
        instance = self.get_model_obj(username)
        if not instance:
            return Response({'status': 0, 'msg': '传入正确的id,没有这个对象'})
        is_right_ver = self.only_check_ver(username, ver)
        if is_right_ver['status'] == 1:
            instance.set_password(new_passwd)
            instance.save()
            return Response({'status': 1, 'msg': '修改成功'})
        elif is_right_ver['status'] == 0:
            return Response(is_right_ver)

    # 密码修改
    def change_passwd(self, request):
        user = request.user
        data = request.data
        new_passwd = data.get('new_passwd', None)
        re_new_passwd = data.get('re_new_passwd', None)
        old_passwd = data.get('old_passwd', None)
        if re_new_passwd != new_passwd:
            return Response({'status': 0, 'msg': '两次密码不相等,朋友~智商是个好东西,希望你也能拥有...'})
        is_u = auth.authenticate(username=user.username, password=old_passwd)
        if is_u:
            user.set_password(new_passwd)
            user.save()
        else:
            return Response({'status': 0, 'msg': '请输入正确的原密码,如果您不记得你的原配.就直接用邮件或短信告诉我,我帮你修了Ta...不用谢,我是雷锋..'})

    #后台管理users
    #冻结
    def freezen_user(self,request):
        username=request.data.get('username',None)
        if username:
            instance =  self.get_model_obj(username)
            if not instance:
                return Response({'status': 0, 'msg': '传入正确的id,没有这个对象'})
            instance.status = 1
            instance.save()
            return Response({'status':1,'msg':'冻结成功'})
        else:
            return Response({'status': 0, 'msg': '没有此对象'})

    #解冻
    def thaw(self,request):
        username = request.data.get('username', None)
        if username:
            instance = self.get_model_obj(username)
            if not instance:
                return Response({'status': 0, 'msg': '传入正确的id,没有这个对象'})
            instance.status = 2
            instance.save()
            return Response({'status': 1, 'msg': '冻结成功'})
        else:
            return Response({'status': 0, 'msg': '没有此对象'})

    #删除
    def delete_user(self,request):
        username = request.data.get('username', None)
        if username:
            instance = self.get_model_obj(username)
            if not instance:
                return Response({'status': 0, 'msg': '传入正确的id,没有这个对象'})
            instance.status = 3
            instance.save()
            return Response({'status': 1, 'msg': '冻结成功'})
        else:
            return Response({'status': 0, 'msg': '没有此对象'})

    #获取全部用户
    def get_group_user(self,request):
        group = Group.objects.get(id=1)
        users = group.user.all()
        serializer = serializers.UserSerializer(users,many=True).data
        return Response({'status':1,'data':serializer})

    #获取社区管理员
    def get_group_user(self,request):
        group = Group.objects.get(id=2)
        users = group.user.all()
        serializer = serializers.UserSerializer(users,many=True).data
        return Response({'status':1,'data':serializer})

    # 获取超级管理员
    def get_group_user(self,request):
        group = Group.objects.get(id=3)
        users = group.user.all()
        serializer = serializers.UserSerializer(users,many=True).data
        return Response({'status':1,'data':serializer})

    # 按类型筛选用户
    def screen_group_user(self,request):
        type = request.data.get('type',None)
        if type:
            group = Group.objects.get(id=3)
            users = group.user.all()
            serializer = serializers.UserSerializer(users,many=True).data
            return Response({'status':1,'data':serializer})
        else:
            return Response({'status':0,'msg':'选择合适类型'})

    #根据用户名，真实姓名，和邮箱查找用户
    def search_user(self,request):
        user = request.user
        ser_content = request.data.get('ser_content',None)
        if user.type ==3:
            if ser_content:
                users = User.objects.filter(Q(username__contains=ser_content)|Q(real_name__contains=ser_content)|Q(email__contains=ser_content))
            else:
                users = User.objects.all()
        elif  user.type ==2:
            if ser_content:
                users = User.objects.filter(Q(username__contains=ser_content)|Q(real_name__contains=ser_content)|Q(email__contains=ser_content))
            else:
                users = User.objects.filter(belong_to_community=user.get_community())
        else:
            return Response({'status':0,'msg':'不好意思,小朋友,你们没有权限'})
        serializer = self.get_serializer(users, many=True).data
        return Response({'status': 1, 'data': serializer})







