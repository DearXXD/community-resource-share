# coding:utf-8
from accounts.models import User
from rest_framework import serializers
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''用户序列化'''
    class Meta:
        model = User
        fields = ['id','username']

class UserSerializerR(serializers.HyperlinkedModelSerializer):
    '''用户序列化'''
    id = serializers.IntegerField(required=False)
    cart = serializers.ListField(required=False,read_only=True)
    class Meta:
        model = User
        fields = ['id','username','address','id_card','email','real_name','cart','integration','join_time']
