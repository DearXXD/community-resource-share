# coding:utf-8
from django.shortcuts import render
from ce.tasks import *
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


