# coding:utf-8
import hashlib
import datetime
import httplib
import urllib,urllib2
import calendar,time
from django.http import HttpResponse
from random import random,randint,Random
import os
import json
# print {k: v for k, v in os.environ.items() if k.lower().endswith('_proxy')}

def s_message(mobiles,params):
    url = 'https://api.netease.im/sms/sendtemplate.action'
    templateid = 3032484
    AppKey = '01ee913d759b9f09d6114b79c2470f8a'
    Nonce = str(random())
    AppSecret = 'fe8fcc004513'
    CurTime =str(time.mktime(datetime.datetime.now().timetuple()))
    CheckSum = hashlib.sha1(AppSecret + Nonce + CurTime).hexdigest()
    headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8','AppKey':AppKey,'Nonce':Nonce,'CurTime':CurTime,'CheckSum':CheckSum}
    data = {
        'mobiles':mobiles,
        'params':params,
        'templateid':templateid
    }
    new_params = map(lambda x:urllib.quote(x), params)
    url_data = 'mobiles='+str(mobiles)+'&'+'params='+str(new_params)+'&'+'templateid='+str(templateid)
    req = urllib2.Request(url, url_data, headers=headers)
    req.headers
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

#提醒
def s_message_t(mobiles,params):
    url = 'https://api.netease.im/sms/sendtemplate.action'
    templateid = 3030479
    AppKey = '01ee913d759b9f09d6114b79c2470f8a'
    Nonce = str(random())
    AppSecret = 'fe8fcc004513'
    CurTime =str(time.mktime(datetime.datetime.now().timetuple()))
    CheckSum = hashlib.sha1(AppSecret + Nonce + CurTime).hexdigest()
    headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8','AppKey':AppKey,'Nonce':Nonce,'CurTime':CurTime,'CheckSum':CheckSum}
    data = {
        'mobiles':mobiles,
        'params':params,
        'templateid':templateid
    }
    new_params = map(lambda x:urllib.quote(x), params)
    url_data = 'mobiles='+str(mobiles)+'&'+'params='+str(new_params)+'&'+'templateid='+str(templateid)
    req = urllib2.Request(url, url_data, headers=headers)
    req.headers
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

#通知
def s_message_notice(mobiles,params):
    url = 'https://api.netease.im/sms/sendtemplate.action'
    templateid = 3038021
    AppKey = '01ee913d759b9f09d6114b79c2470f8a'
    Nonce = str(random())
    AppSecret = 'fe8fcc004513'
    CurTime =str(time.mktime(datetime.datetime.now().timetuple()))
    CheckSum = hashlib.sha1(AppSecret + Nonce + CurTime).hexdigest()
    headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8','AppKey':AppKey,'Nonce':Nonce,'CurTime':CurTime,'CheckSum':CheckSum}
    data = {
        'mobiles':mobiles,
        'params':params,
        'templateid':templateid
    }
    new_params = map(lambda x:urllib.quote(x), params)
    url_data = 'mobiles='+str(mobiles)+'&'+'params='+str(new_params)+'&'+'templateid='+str(templateid)
    req = urllib2.Request(url, url_data, headers=headers)
    req.headers
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res