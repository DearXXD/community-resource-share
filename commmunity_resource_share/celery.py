# encoding:utf-8
from __future__ import absolute_import
import os,django
from django.conf import settings
from celery import Celery,platforms

platforms.C_FORCE_ROOT = True  #以root权限
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commmunity_resource_share.settings')

app = Celery('accounts',backend='amqp://guest@localhost//', broker='amqp://guest@localhost//',include=['ce.tasks'])
app.config_from_object('commmunity_resource_share.config')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# app.conf.update(
#     # CELERY_TASK_RESULT_EXPIRES=1,
#     CELERY_RESULT_SERIALIZER='json',
# )
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()