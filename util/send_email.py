# -*- coding:utf-8 -*-

import requests
import os
from django.shortcuts import HttpResponse, render_to_response, render,HttpResponseRedirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_email(to, subject, content, fromname, from_email, identity):

    url = "http://sendcloud.sohu.com/webapi/mail.send.json"

    # 不同于登录SendCloud站点的帐号，您需要登录后台创建发信子帐号，使用子帐号和密码才可以进行邮件的发送。
    params = {"api_user": "yy00900_test_APb7dt",
              "api_key": "CHcAw7LOWaWkT6fC",
              "templateInvokeName": "send_resume_template",
              "from": from_email,
              "fromname": fromname,
              "to": to,
              "subject": subject,
              "html": content,
              "resp_email_id": "true"
              }

    filename1 = "resume_%s.pdf" % identity
    files = {"file1": (filename1, open("/home/www/manibang_app/resume_%s.pdf" % identity, "rb"))}

    r = requests.post(url, files=files, data=params)

    print r.text


def setEmail(subject,form_email,to,html_content):

    #        方式一：
    #         send_mail('subject', 'this is the message of email', 'pythonsuper@gmail.com', ['1565208411@qq.com','1373763906@qq.com'], fail_silently=True)

    #        方式二：
    #         message1 = ('subject1','this is the message of email1','pythonsuper@gmail.com',['1565208411@qq.com','xinxinyu2011@163.com'])
    #         message2 = ('subject2','this is the message of email2','pythonsuper@gmail.com',['1373763906@qq.com','xinxinyu2011@163.com'])
    #         send_mass_mail((message1,message2), fail_silently=False)

    #        方式三：防止邮件头注入
    #         try:
    #             send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection)
    #         except BadHeaderError:
    #             return HttpResponse('Invaild header fount.')

    #        方式四：EmailMessage()
    # 首先实例化一个EmailMessage()对象
    #         em = EmailMessage('subject','body','from@example.com',['1565208411@qq.com'],['xinxinyu2011@163.com'],header={'Reply-to':'another@example.com'})
    # 调用相应的方法

    #         方式五：发送多用途邮件
    # subject, form_email, to = 'hello', '13540354036@163.com', '13540354036@163.com'
    text_content = 'This is an important message'
    # html_content = u'<b>激活链接：</b><a href="http://www.baidu.com">http:www.baidu.com</a>'
    msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    #       发送邮件成功了给管理员发送一个反馈
    #mail_admins(u'用户注册反馈', u'当前XX用户注册了该网站', fail_silently=True)

