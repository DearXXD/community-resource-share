# coding:utf-8
from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import  Resource,Category,Respic
from community.serializers import CommunityIdSerializer

class RespicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Respic
        fields = ('id','pic')

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    focus = serializers.CharField(source='focus.count',required=False)
    # master = serializers.StringRelatedField(source='master.username')
    master = UserSerializer(read_only=True, required=False)
    community = CommunityIdSerializer(read_only=True, required=False)
    pic = serializers.ListField(required=False)
    picList = serializers.ListField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name='api_resources:resource-detail')
    class Meta:
        model = Resource
        fields = ('id', 'description', 'master', 'resource_picture',
                  'name', 'create_time', 'create_time', 'use_time','url','community',
                  'return_time', 'intergration', 'is_active', 'is_used','focus','pub_address','pic','picList','rate','rate_content')

class ResourceWithoutUserSerializer(serializers.HyperlinkedModelSerializer):
    # pic = serializers.ListField(required=False)
    class Meta:
        model = Resource
        fields = ('id', 'description', 'resource_picture',
                  'name', 'create_time', 'create_time', 'use_time',
                  'return_time', 'intergration', 'is_active', 'is_used','pub_address')

# class ResourceWithoutIdSerializer(serializers.HyperlinkedModelSerializer):
#     pic = serializers.ListField(required=False)
#     class Meta:
#         model = Resource
#         fields = ('id', 'description', 'resource_picture',
#                   'name', 'create_time', 'create_time', 'use_time',
#                   'return_time', 'intergration', 'is_active', 'is_used','pub_address')


class CategoryWithoutParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','create_time','layer','can_delete')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parent = CategoryWithoutParentSerializer()
    class Meta:
        model = Category
        fields = ('id','name','create_time','parent','layer','can_delete')
