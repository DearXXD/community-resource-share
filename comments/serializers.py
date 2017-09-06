# coding:utf-8
from rest_framework import serializers
from comments.models import Comment
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """评论序列化类"""
    author = UserSerializer(read_only=True, required=False)
    object_id = serializers.IntegerField(read_only=True, required=False)
    content_type_id = serializers.IntegerField(read_only=True, required=False)
    class Meta:
        order_by = 'dateline'
        model = Comment
        fields = ('id', 'text', 'author', 'dateline','object_id','content_type_id')  #TODO 未完全序列化