# -*- coding:utf-8 -*-
import httplib
import urllib
from random import randint
import json
from random import random,randint,Random
from django.http import JsonResponse,HttpResponse
#服务地址
sms_host = "sms.yunpian.com"
voice_host = "voice.yunpian.com"
#端口号
port = 443
#版本号
version = "v1"
#查账户信息的URI
user_get_uri = "/" + version + "/user/get.json"
#智能匹配模板短信接口的URI
sms_send_uri = "/" + version + "/sms/send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"
#语音短信接口的URI
sms_voice_send_uri = "/" + version + "/voice/send.json"

apikey = "6c808c1a278b2fbbd1994e3fca971d24"


def get_user_info(apikey=apikey):
    """
    取账户信息
    """
    conn = httplib.HTTPSConnection(sms_host, port=port)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request('POST',user_get_uri,urllib.urlencode( {'apikey' : apikey}))
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def send_sms(text, mobile):
    """
    通用接口发短信（您的验证码是。。。。）text为短信内容，mobile为电话号码
    """
    apikey = "6c808c1a278b2fbbd1994e3fca971d24"
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def get_code():
    TOTAL = '0123456789'
    TOTAL_LENGTH = len(TOTAL)
    CODE_LENGTH = 6

    random = Random()
    verification = ''

    for i in range(CODE_LENGTH):
        verification += TOTAL[random.randint(0, TOTAL_LENGTH - 1)]
    return verification
