# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery
from celery import platforms #从celery导入Celery的应用程序接口

platforms.C_FORCE_ROOT = True

app = Celery('celery_set', #首先创建了一个celery实例app,实例化的过程中，制定了任务名pj(与当前文件的名字相同)，Celery的第一个参数是当前模块的名称，我们可以调用config_from_object()来让Celery实例加载配置模块
             broker = 'redis://127.0.0.1:6379/5',#设置中间人
             backend= 'redis://127.0.0.1:6379/6',#设置后端，显示异常和回朔
             include= ['celery_set.tasks']
            )

app.config_from_object('celery_set.config')#从config.py中导入配置文件
if __name__ == '__main__':  #执行当前文件，运行celery
    app.start()