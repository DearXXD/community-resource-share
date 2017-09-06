# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_auto_20170329_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 5, 37, 57, 653937, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='pic',
            field=models.ManyToManyField(to='resources.Respic', null=True, verbose_name='\u5173\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 5, 37, 57, 653997, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
        migrations.AlterField(
            model_name='respic',
            name='pic',
            field=models.ImageField(upload_to=b'resource_pic/%Y/%m/%d', verbose_name='\u7269\u54c1\u7167\u7247'),
        ),
    ]
