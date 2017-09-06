# encoding:utf-8
from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "commmunity_resource_share.settings")
CELERY_TIMEZONE = 'Asia/Shanghai'


#任务的优先级问题，在这个例子中如果我们想让add这个加法任务优先于subtract减法任务被执行，我们可以将两个任务放到不同的队列中，由我们决定先执行哪个任务，我们可以在配置文件中这样配置：
# CELERY_ROUTES = {
#     'ce.tasks.check_who_has_order':{'queue':'for_add','routing_key':'for_add'},
#     # 'celery_set.tasks.subtract':{'queue':'for_subtract','routing_key':'for_subtract'},
#     # 'celery_set.tasks.download_file_as_category':{'queue':'for_down','routing_key':'for_down'},
# }


#celery的beat去周期的生成任务和执行任务，在这个例子中我希望每10秒钟产生一个任务，然后去执行这个任务，
CELERYBEAT_SCHEDULE = {
    'check_who_has_order':{
            'task':'ce.tasks.check_who_has_order',         #指定执行的任务的位置
            'schedule':timedelta(seconds=60*60*23),   #指定执行的时间间隔
            # 'args':(100,100)                    #传入add()的参数
    },
    'send_notifi': {
        'task': 'ce.tasks.send_notifi',  # 指定执行的任务的位置
        'schedule': timedelta(seconds=10),  # 指定执行的时间间隔
    }
}