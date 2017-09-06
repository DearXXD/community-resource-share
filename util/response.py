# coding:utf-8
from rest_framework.response import Response
from django.http import Http404

def get_obj(insatnce_class,id):
    '''
    获取对象
    :param insatnce_class:对象类名
    :param id:对象id
    :return:对象实例
    '''
    if not id or not insatnce_class:
        return None
    try:
        instance = insatnce_class.objects.get(id=id)
    except insatnce_class.DoesNotExist:
        raise Http404(u'对象不存在')
    return instance

class JsonResponse(Response):
    CODE_SUCC = 200  # 成功
    CODE_404 = 404 # 没有找到
    CODE_NO_PERMISSION = 422 # 没有找到
    CODE_ERROR = 500  # 错误
    CODE_ERROR_DATA = 502  # 数据错误
    CODE_ERROR_PASS = 501  # 用户名或密码错误
    def __init__(self, msg=u'', code=200, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None, other_dict= {}):
        # data = {"data": data} if data else {}
        data = {"data": data}
        data['code'] = code
        data['msg'] = msg
        data['status'] = status
        if other_dict:
            data.update(other_dict)
        super(JsonResponse, self).__init__(data,  template_name, headers, exception, content_type)