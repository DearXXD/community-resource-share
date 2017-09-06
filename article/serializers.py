# coding:utf-8
from article.models import Article, ArticleCategory
from rest_framework import serializers

class ArticleCategoryNameSerializer(serializers.HyperlinkedModelSerializer):
    """文章分类的序列化"""
    class Meta:
        model = ArticleCategory
        fields = ('id', 'name')

class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
    """文章的序列化"""
    # category = serializers.StringRelatedField()
    category = ArticleCategoryNameSerializer(required=False,many=True)
    author =serializers.StringRelatedField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name="api_articles:article-detail")
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'is_top', 'category', 'cover_img', 'dateline', 'url','text')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    """文章的序列化"""
    category = serializers.StringRelatedField()
    author =serializers.StringRelatedField(required=False)
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'text', 'is_top', 'category', 'cover_img', 'dateline')

class BaseArticleCategorySerializer(serializers.HyperlinkedModelSerializer):
    """文章分类的序列化基类"""
    class Meta:
        model = ArticleCategory
        fields = ('id', 'name')

class ArticleCategorySerializer(serializers.HyperlinkedModelSerializer):
    """文章分类的序列化"""
    parent = serializers.StringRelatedField(required=False)
    parent_id = serializers.IntegerField(required=False)
    class Meta:
        model = ArticleCategory
        fields = ('id', 'parent', 'parent_id', 'name')

class ArticleCategoryWithChildrenSerializer(serializers.HyperlinkedModelSerializer):
    """带详细子分类的"""
    children = BaseArticleCategorySerializer(required=False, many=True)
    class Meta:
        model = ArticleCategory
        fields = ('id', 'children', 'name')