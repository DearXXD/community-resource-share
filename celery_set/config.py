# coding:utf-8
from __future__  import absolute_import
from datetime import timedelta
from celery import Celery
from  celery import group
from celery.schedules import crontab
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "commmunity_resource_share.settings")


#任务的优先级问题，在这个例子中如果我们想让add这个加法任务优先于subtract减法任务被执行，我们可以将两个任务放到不同的队列中，由我们决定先执行哪个任务，我们可以在配置文件中这样配置：
CELERY_ROUTES = {
    'accounts.tasks.add':{'queue':'for_add','routing_key':'for_add'},
    # 'celery_set.tasks.subtract':{'queue':'for_subtract','routing_key':'for_subtract'},
    # 'celery_set.tasks.download_file_as_category':{'queue':'for_down','routing_key':'for_down'},
}


#celery的beat去周期的生成任务和执行任务，在这个例子中我希望每10秒钟产生一个任务，然后去执行这个任务，
CELERYBEAT_SCHEDULE = {
    'add':{
            'task':'accounts.tasks.add',             #指定执行的任务的位置
            'schedule':timedelta(seconds=30),   #指定执行的时间间隔
            'args':(100,100)                    #传入add()的参数
    },
    #更近一步，如果我希望在每周四的19点30分生成任务，分发任务，让worker取走执行，可以这样配置：
    'subtract':{
            'task':'celery_set.task.subtract',
            'schedule':crontab(hour=10,minute=52,day_of_week=5),
            'args':(100,300)
    },
    # 'download_file_as_category':{
    #         'task':'celery_set.task.download_file_as_category',
    #         'schedule':crontab(hour=10,minute=52,day_of_week=5),
    #         'args':(100,300)
    # },

}
CELERY_TIMEZONE = 'Asia/Shanghai'  #指定时区
#执行命令: celery -A pro worker -B -Q for_add -l info  注意：加　－Ｂ地定时任务，－Ａ指定执行的ａｐｐ，－Ｑ指定执行的队列 ,-l 日志的等级
