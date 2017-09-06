# encoding:utf-8
from django.conf.urls import url,include
from .views import ContactViewset

urlpatterns = [
    url(r'create_contact/$', ContactViewset.as_view({'post':'create'})),
]