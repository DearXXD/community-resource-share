# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0015_auto_20170413_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='picList',
            field=accounts.fields.ListField(max_length=100, null=True, verbose_name='\u8bc4\u4ef7\u56fe\u7247', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rate',
            field=models.CharField(max_length=10, null=True, verbose_name='\u8bc4\u5206', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='rate_content',
            field=models.TextField(null=True, verbose_name='\u8bc4\u4ef7\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 15, 10, 3, 51, 965710, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 10, 3, 51, 965767, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
