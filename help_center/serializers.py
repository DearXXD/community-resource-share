# coding:utf-8
from help_center.models import *
from rest_framework import serializers
from accounts.serializers import UserSerializer

class Help_categorySerializers(serializers.HyperlinkedModelSerializer):
    '''类别序列化'''
    class Meta:
        model = Help_category
        fields = ('id','name')


class Help_articeSerializers(serializers.HyperlinkedModelSerializer):
    '''文章的序列化'''
    user = UserSerializer()
    category = Help_categorySerializers()
    class Meta:
        model= Help_article
        fields = ('id','title','content','document','document_name' ,'category','user','create_time')