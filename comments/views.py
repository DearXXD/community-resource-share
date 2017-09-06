# coding:utf-8
from django.http import Http404
from util.response import JsonResponse
from comments.models import Comment
from comments.serializers import CommentSerializer
from util.viewset import ViewSet
from util.mixin import GenericMethodMixin,CommentMixin
from util.response import JsonResponse,get_obj
from django.contrib.contenttypes.models import ContentType

class CommentViewSet(ViewSet,GenericMethodMixin,CommentMixin):
    """评论管理"""
    queryset = Comment.objects.all().order_by('-dateline')
    serializer_class = CommentSerializer
    model_class = Comment

    def delete(self, request, pk):
        try:
            comment = Comment.objects.filter(id=pk)
        except Comment.DoesNotExist:
            raise Http404(u'评论不存在')
        comment.delete()
        return JsonResponse(msg=u'删除成功')

    def get_comment_comments(self, request,pk):
        """
        获取我的评论,时间逆序访问
        :param request:
        :return:
        """
        obj=get_obj(self.model_class,pk)
        com = ContentType.objects.get(app_label="comments")
        comments = self.queryset.filter(object_id=pk,content_type_id=com.id)
        serializer = self.get_serializer(comments,many=True).data
        return JsonResponse('ok',data=serializer,status=1)



