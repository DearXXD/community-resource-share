#coding:utf-8
from celery import Celery
from celery_set.celery import app
import os,sys, tarfile
import shutil

@app.task
def add(x,y):
    return x+y

@app.task
def subtract(x, y):
    return x - y
#执行命令: celery -A tasks worker --loglevel=info

