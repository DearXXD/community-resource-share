# encoding:utf-8
import random
from commmunity_resource_share.celery import app
from util.msg import s_message_t
@app.task
def add(a,b):
    return a+b

@app.task
def send():
    # s_message_t(['13438326909','13438811615','13540354036'], ['asjdhjkasbdnjk'])
    a = s_message_t(["13438811615"], ["ttfirm", "username", "today", "meass"])
    print a
    return 12