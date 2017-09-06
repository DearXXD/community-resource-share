# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_auto_20170309_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 3, 36, 38, 470087, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(max_length=500, verbose_name='\u7269\u54c1\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='focus',
            field=models.ManyToManyField(related_name='focus', null=True, verbose_name='\u5173\u6ce8', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 3, 36, 38, 470169, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
