# coding:utf8
from accounts.models import User
from .response import JsonResponse
def is_login_require():
    """
    权限装饰器
    后台:is_ａｄｍｉｎ
    """
    def _deco(func):
        def __deco(instance, request, *args, **kwargs):
            user = request.user
            if user.is_anonymous():
                return JsonResponse( u'您还没有登录，请登录!', status=0)
            return func(instance, request, *args, **kwargs)
        return __deco
    return _deco