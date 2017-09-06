"""commmunity_resource_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import UserVewSet,login_html
# from django.accounts import

urlpatterns = [
    # url(r'^regist/(?P<username>[0-9]+)/(?P<password>[0-9]+)/', regist),
    # url(r'^read_from_cache/', read_from_cache),
    # # url(r'^test/(?P<c>[0-9]+)/(?P<d>[0-9]+)/', test),
    # url(r'^tes/(?P<u>[0-9]+)/(?P<p>[0-9]+)/', tes),
    url(r'userinfo/', UserVewSet.as_view({'get': 'get_user_info'})),
    url(r'login',UserVewSet.as_view({'post':'user_login'})),
    url(r'logout',UserVewSet.as_view({'get':'user_logout'})),
    url(r'regist/(?P<community_id>[0-9]+)/',UserVewSet.as_view({'post':'regist'})),
    url(r'add_cart/(?P<resource_id>[0-9]+)/',UserVewSet.as_view({'get':'add_cart'})),
    url(r'get_cart_list/',UserVewSet.as_view({'get':'get_cart_list'})),
    url(r'remove_cart/',UserVewSet.as_view({'post':'remove_cart'})),
    url(r'get_username/',UserVewSet.as_view({'get':'get_username'})),
    url(r'updata_user/',UserVewSet.as_view({'post':'updata_user'})),

]
