# coding:utf-8
from __future__ import absolute_import
from celery import shared_task
import os,sys, tarfile
import shutil,time
import datetime
import random
from commmunity_resource_share.celery import app
from django.http import HttpResponse
from send_email_message.msg import s_message_t
from send_email_message.send_email import setEmail
from django.utils import timezone
from accounts.models import User
from order.models import Order
from article.models import Article
import sys,datetime
from django.db.models import Q
reload(sys)
sys.setdefaultencoding('utf8')

#自动发送短信
@app.task
def auto_send_msg_ye(remind_l):
    for remind in remind_l:
        content = []
        content.append(remind['firm_name'])
        content.append(remind['remind_time'])
        content.append(remind['case'])
        content.append(remind['content'])
        s_message_t(remind['phone'],content)
    return 'ok'

@app.task
def send_notifi():
    arts = Article.objects.filter(dateline__gte=datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day, 0, 0, 0))
    users = User.objects.all()
    for user in users:
        if user.email:
            if arts:
                subject = '社区资源共享'
                form_email = '13540354036@163.com'
                html_content = '您今天有新的社区公告,请您查看,及时做好生活安排'
                try:
                    setEmail(subject, form_email, user.email, html_content)
                except:
                    pass
    return 'ok'

@app.task
def send_email_tt(user):
    subject = '社区资源共享'
    form_email = '13540354036@163.com'
    html_content = '【社区资源共享】欢迎您注册成为社区的一员'
    setEmail(subject, form_email, user.email, html_content)


@app.task
def check_who_has_order():
    subject = '社区资源共享'
    form_email = '13540354036@163.com'
    html_content = '【社区资源共享】您有订单正在使用中,使用过程中请注意自身安全,请爱护资源'
    orders = Order.objects.filter(process=3)
    for order in orders:
        setEmail(subject, form_email, order.buyer.email, html_content)