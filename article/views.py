# coding:utf-8
from django.db.models import QuerySet
from django.http import Http404
from util.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from comments.models import Comment
from comments.serializers import CommentSerializer
from article.models import Article, ArticleCategory
from article.serializers import (ArticleCategorySerializer, ArticleSerializer, ArticleCategoryWithChildrenSerializer,
ArticleListSerializer)
from util.mixin import PageReponseMixin,GenericMethodMixin,CommentMixin
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

class ArticleCategoryViewSet(viewsets.ModelViewSet):
    """文章分类创建"""
    queryset = ArticleCategory.objects.filter(parent=None)
    serializer_class = ArticleCategorySerializer
    model_class=ArticleCategory

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(data=serializer.data, headers=headers)

    @detail_route(['get'])
    def category_detail(self, request, pk):
        article_category = ArticleCategory.objects.get(id=pk)
        serializer = ArticleCategoryWithChildrenSerializer(article_category)
        return JsonResponse(data=serializer.data)

class ArticleAuthenticatedViewSet(viewsets.ModelViewSet, PageReponseMixin,GenericMethodMixin,CommentMixin):
    """文章视图"""
    queryset = Article.objects.all().order_by('-dateline')
    serializer_class = ArticleListSerializer
    permission_classes = IsAuthenticated
    model_class=Article

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(u'数据错误',JsonResponse.CODE_ERROR_DATA,data=serializer.errors)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(data=serializer.data, headers=headers)

    def comment_article(self, request, pk):
        """评论文章"""
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            raise Http404('Article doesnot exist')
        data = request.data
        text = data.get('text')
        if not text:
            return JsonResponse(msg=u'数据不能为空', code=JsonResponse.CODE_ERROR)
        user = request.user
        comment = Comment(content_object=article, text=text, author=user)
        comment.save()
        serializer = CommentSerializer(comment)
        return JsonResponse(msg=u'评论成功', data=serializer.data)

class ArticleViewSet(viewsets.ModelViewSet, PageReponseMixin,GenericMethodMixin,CommentMixin):
    """文章视图"""
    queryset = Article.objects.all().order_by('-dateline')
    serializer_class = ArticleListSerializer
    model_class=Article

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return self.get_paginated_response_status(request, queryset)

    # @detail_route(['get'])
    # def detail(self, request, pk):
    #     """获取文章详情"""
    #     try:
    #         article = Article.objects.get(id=pk)
    #     except Article.DoesNotExist:
    #         raise Http404('Article doesnot exist')
    #     serializer = ArticleSerializer(article)
    #     return JsonResponse(data=serializer.data)

    def search(self, request):
        """
        搜索文章，按照标题， 类型， 内容搜索
        :param request:
        :return:
        """
        s = request.data.get('s')
        category = request.data.get('category')
        q = Q(title__contains=s)
        q |= Q(author__username__contains=s)
        # q |= Q(category)
        article_set = Article.objects.filter(q)
        serializer = ArticleSerializer(article_set, many=True)
        return JsonResponse(data=serializer.data)
