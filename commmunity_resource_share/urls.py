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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import admin
# admin.autodiscover()
import xadmin as admin
from accounts.views import login_html
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/accounts/', include('accounts.urls')),
    url(r'^api/community/', include('community.urls',namespace='api_community')),
    url(r'^api/resources/', include('resources.urls',namespace='api_resources')),
    url(r'^api/order/', include('order.urls',namespace='api_order')),
    url(r'^api/article/', include('article.urls',namespace='api_articles')),
    url(r'^api/contact/', include('contact.urls',namespace='api_contact')),
    url(r'^api/comments/', include('comments.urls',namespace='api_comments')),
    url(r'^$', login_html)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)