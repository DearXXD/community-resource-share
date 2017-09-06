# coding:utf-8
from rest_framework import viewsets
from util.mixin import PageReponseMixin,GenericMethodMixin
from util.response import JsonResponse

class ViewSet(viewsets.ModelViewSet, PageReponseMixin, GenericMethodMixin):
    """
    帖子分类
    """
    queryset = None
    serializer_class = None
    model = None
    detail_serializer_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return self.get_paginated_response_status(request, queryset)

    def create(self, request, *args, **kwargs):
        serializer_class = kwargs.pop('serializer_class', None)
        assert serializer_class or self.serializer_class, (u'serializer_class cannot be none!')
        serializer = self.serializer_class(data=request.data) if not serializer_class \
            else serializer_class(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(code=JsonResponse.CODE_ERROR_DATA, data=serializer.errors)
        serializer.save()
        return JsonResponse(msg=u'成功')
