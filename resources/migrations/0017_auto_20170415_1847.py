# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0016_auto_20170415_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 15, 10, 47, 55, 201560, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='pic',
            field=accounts.fields.ListField(default=[]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='picList',
            field=accounts.fields.ListField(null=True, verbose_name='\u8bc4\u4ef7\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 10, 47, 55, 201614, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
