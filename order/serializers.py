# coding:utf-8
from rest_framework import serializers
from .models import  Order
from accounts.models import User
from community.models import Community
from resources.models import Resource
from accounts.serializers import UserSerializer

class SimpleCommunity(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name')

class SimpleResource(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'intergration' ,'resource_picture', 'name','create_time')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    master = UserSerializer(read_only=True, required=False)
    buyer = UserSerializer(read_only=True, required=False)
    community_id = serializers.IntegerField(read_only=True, required=False)
    resource_id = serializers.IntegerField(read_only=True, required=False)
    order_number = serializers.IntegerField(read_only=True, required=False)
    process = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'order_number', 'intergration' , 'master' , 'resource_id' , 'buyer' ,'community_id', 'is_complete' ,'is_damage','damage_pic' ,'process','begin_time','end_time')

    def save(self, *args, **kwargs):
        """保存"""
        community_id = kwargs.get('community_id',None)
        master_id = kwargs.get('master_id',None)
        buyer = kwargs.get('user',None)
        resource_id = kwargs.get('resource_id',None)
        order_number = kwargs.get('order_number',None)
        self.community_id = community_id
        self.master_id = master_id
        self.buyer = buyer
        self.order_number = order_number
        self.resource_id = resource_id
        super(OrderSerializer, self).save(*args, **kwargs)


class OrderWithAllSerializer(serializers.HyperlinkedModelSerializer):
    master = UserSerializer(read_only=True, required=False)
    buyer = UserSerializer(read_only=True, required=False)
    community = SimpleCommunity(read_only=True, required=False)
    resource = SimpleResource(read_only=True, required=False)
    order_number = serializers.IntegerField(read_only=True, required=False)
    process = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'order_number', 'intergration', 'master', 'resource', 'buyer', 'community', 'is_complete',
                  'is_damage', 'damage_pic', 'process', 'begin_time', 'end_time')