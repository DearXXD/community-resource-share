# coding:utf-8
from django.http import Http404
from util.response import JsonResponse
from collections import OrderedDict
from comments.models import Comment
from comments.serializers import CommentSerializer
from django.db.models import Q
from util.response import get_obj
from django.contrib.contenttypes.models import ContentType

class PageReponseMixin(object):
    def get_paginated_response_status(self, request, queryset, serializer_class=None, context=None,status=None):
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True) if not serializer_class \
            else serializer_class(page, context={'request':request}, many=True)
        other_dict = OrderedDict([
        ('count', self.paginator.page.paginator.count),
        ('next', self.paginator.get_next_link()),
        ('previous', self.paginator.get_previous_link()),
        ])
        return JsonResponse(data=serializer.data, other_dict=other_dict,status=status)

class GenericMethodMixin(object):
    def detail(self, request, pk):
        obj = get_obj(self.model_class,pk)
        serializer = self.serializer_class(obj, context={'request': request})
        return JsonResponse(data=serializer.data,status=1)

    def delete(self, request, pk):
        obj = get_obj(self.model_class,pk)
        obj.delete()
        return JsonResponse(msg=u'删除成功',status=1)

    def delete_list(self, request):
        data = request.data
        pk_list = data.get('pk_list',[])
        queryset = self.model_class.objects.filter(id__in=pk_list)
        queryset.delete()
        return JsonResponse(msg=u'删除成功',status=1)

    def search(self, request):
        '''
        精确搜索
        :param request:
        :return:
        '''
        data = request.data
        q = Q(**data)
        obj_set = self.model_class.objects.filter(q)
        serializer = self.serializer_class(obj_set, context={'request': request}, many=True)
        return JsonResponse(data=serializer.data,status=1)

    def search_obj(self,request):
        '''
        按名字搜索，模糊匹配
        :param request: 搜索条件
        :return: 搜索结果
        '''
        search_content = request.data.get('s',None)
        if not search_content:
            return JsonResponse(msg='数据错误，缺少参数',code=502,status=0)
        instances = self.model_class.objects.filter(name__contains=search_content)
        serializer = self.get_serializer(instances,many=True,context={'request': request})
        return JsonResponse(msg='ok',data=serializer.data,status=1)

    def sort_obj(self,request):
        '''
        按任意属性排序
        :param request: 排序方式
        获取排序方式
        排序
        :return:排序结果
        '''
        sort_way = request.data.get('sort_way',None)
        # print sort_way,dir(self.model_class)
        # print self.model_class.__dict__.keys()
        # print self.model_class._meta.fields
        fs = [f.name for f in self.model_class._meta.fields]
        if not sort_way:
            serializer = self.get_serializer(self.get_queryset(),many=True)
            return JsonResponse(msg='ok',data=serializer.data,status=1)
        if sort_way not in fs:
            return JsonResponse(msg='没有这个排序方式',code = 404,status=0)
        serializer = self.get_serializer(self.get_queryset().order_by('-'+sort_way),many=True)
        return JsonResponse(msg='ok', data=serializer.data, status=1)

    def modify(self, request, id):
        '''
        修改信息
        :param request:
        :param id:
        :return:
        '''
        data = request.data
        obj = get_obj(self.model_class,id)
        for key in data.keys():
            # print key,data[key]
            obj.__setattr__(key, data[key])
        obj.save()
        return JsonResponse(u'成功',status=1)

class CommunityQuerySetMixin(object):
    '''
    必须和PageResponseMixin一起使用
    '''
    def get_query_set(self, request, community_id):
        queryset = self.model_class.objects.filter(community_id=community_id)
        if not hasattr(self, 'get_paginated_response_status'):
            raise AttributeError(u'必须和PageResponseMixin一起使用')
        return self.get_paginated_response_status(request, queryset, self.serializer_class, context={'request':request})

class CommentMixin(object):
    def comment(self, request, pk):
        user = request.user
        obj = get_obj(self.model_class,pk)
        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(u'数据格式错误', code=JsonResponse.CODE_ERROR_DATA, data=serializer.errors)
        comment = Comment.objects.create(author=user, content_object=obj, **serializer.validated_data)
        serializer = CommentSerializer(comment)
        return JsonResponse(u'ok', data=serializer.data,status=1)

    def comment_list(self, request, pk):
        obj = get_obj(self.model_class,pk)
        content_id = ContentType.objects.get(app_label="comments").id
        queryset = obj.comments.all().order_by('-dateline')
        serializer_class = CommentSerializer
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True) if not serializer_class \
            else serializer_class(page, context={'request': request}, many=True)
        other_dict = OrderedDict([
            ('count', self.paginator.page.paginator.count),
            ('next', self.paginator.get_next_link()),
            ('previous', self.paginator.get_previous_link()),
            ('content_id',content_id),
        ])
        return JsonResponse(data=serializer.data, other_dict=other_dict,status=1)


# class DetailMixin(object):
#     def detail(self, request, pk):
#         obj = get_obj(self.model_class,pk)
#         serializer = self.serializer_class(obj, context={'request': request})
#         return JsonResponse(data=serializer.data)
#
# class DeleteMixin(object):
#     def delete(self, request, pk):
#         obj = get_obj(self.model_class,pk)
#         obj.delete()
#         return JsonResponse(msg=u'删除成功')
#
#     def delete_list(self, request):
#         data = request.data
#         pk_list = data.get('pk_list',[])
#         queryset = self.model_class.objects.filter(id__in=pk_list)
#         queryset.delete()
#         return JsonResponse(msg=u'删除成功')
#
# class SearchMixin(object):
#     def search(self, request):
#         data = request.data
#         q = Q(**data)
#         obj_set = self.model_class.objects.filter(q)
#         serializer = self.serializer_class(obj_set, context={'request': request}, many=True)
#         return JsonResponse(data=serializer.data)
