# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_auto_20170308_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u7c7b\u522b')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('layer', models.IntegerField(default=0, verbose_name='\u5c42\u7ea7')),
                ('can_delete', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x88\xa0\xe9\x99\xa4')),
                ('parent', models.ForeignKey(related_name='child_categories', default=None, blank=True, to='resources.Category', null=True, verbose_name=b'\xe4\xb8\x8a\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95')),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u5206\u7c7b',
                'verbose_name_plural': '\u8d44\u6e90\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=500, verbose_name='\u7269\u54c1\u63cf\u8ff0')),
                ('resource_picture', models.ImageField(upload_to=b'resource_picture/%Y/%m/%d', verbose_name='\u7269\u54c1\u7167\u7247')),
                ('resource_name', models.CharField(max_length=30, verbose_name='\u7269\u54c1\u540d\u5b57')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 3, 8, 11, 40, 40, 612020, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('use_time', models.DateTimeField(default=datetime.datetime(2017, 3, 13, 11, 40, 40, 612137, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True)),
                ('return_time', models.DateTimeField(default=None, null=True, verbose_name='\u5f52\u8fd8\u65e5\u671f', blank=True)),
                ('intergration', models.IntegerField(default=None, null=True, verbose_name='\u6240\u9700\u79ef\u5206', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6fc0\u6d3b\u72b6\u6001')),
                ('is_used', models.BooleanField(default=False, verbose_name='\u662f\u5426\u88ab\u4f7f\u7528')),
                ('pub_address', models.CharField(max_length=25, verbose_name='\u53d1\u5e03\u5730\u5740')),
                ('community', models.ForeignKey(verbose_name='\u7269\u54c1\u6240\u5c5e\u793e\u533a', to='community.Community')),
                ('focus', models.ManyToManyField(related_name='focus', verbose_name='\u5173\u6ce8', to=settings.AUTH_USER_MODEL)),
                ('master', models.ForeignKey(verbose_name='\u7269\u54c1\u6240\u5c5e\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u4e2d\u5fc3',
                'verbose_name_plural': '\u8d44\u6e90\u4e2d\u5fc3',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='resources',
            field=models.ManyToManyField(to='resources.Resource', null=True, verbose_name='\u7c7b\u522b', blank=True),
        ),
    ]
