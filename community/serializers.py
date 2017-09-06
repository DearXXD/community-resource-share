# coding:utf-8
from .models import Community,Province,City,District
from rest_framework import serializers
from accounts.serializers import UserSerializer
#省份的序列化
class ProviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ('id','name')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    """地区模型序列化"""
    class Meta:
        model = City
        fields = ('id', 'name')

class CitySerializerWithProvince(serializers.HyperlinkedModelSerializer):
    """地区模型序列化"""
    province = ProviceSerializer()
    class Meta:
        model = City
        fields = ('id', 'name','province')

    @staticmethod
    def setup_eager_loading(queryset):
        '''预加载'''
        queryset = queryset.prefetch_related('province')
        return queryset


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    """县序列化"""
    class Meta:
        model = District
        fields =('id', 'name')

class DistrictWithCitySerializer(serializers.HyperlinkedModelSerializer):
    """县序列化"""
    city = CitySerializer(required=False)
    class Meta:
        model = District
        fields =('id', 'name', 'city')

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('city')
        return queryset

class CommunityIdSerializer(serializers.HyperlinkedModelSerializer):
    """社区序列化"""
    class Meta:
        model = Community
        fields = (
            ('id', 'name')
        )

class CommunityListSerializer(serializers.HyperlinkedModelSerializer):
    """社区序列化"""
    url = serializers.HyperlinkedIdentityField(view_name='api_community:community-detail')
    manager_id = serializers.IntegerField()
    class Meta:
        model = Community
        fields = (
            ('id', 'name', 'address', 'phone', 'manager_id','url')
        )

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    '''
    社区序完整列化
    '''
    city_id = serializers.IntegerField()
    district_id = serializers.IntegerField()
    province_id = serializers.IntegerField()
    # manager_id = serializers.IntegerField()

    manager = UserSerializer(read_only=True, required=False)
    url = serializers.HyperlinkedIdentityField(view_name='api_community:community-detail')

    class Meta:
        model = Community
        fields = (
            ('id', 'name', 'address', 'phone', 'manager','url','province_id','city_id','district_id','status','email','community_license','community_license_img','join_time')
        )

    @staticmethod
    def setup_eager_loading(queryset):
        '''预加载'''
        queryset = queryset.prefetch_related('manager')
        return queryset

