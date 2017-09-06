# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20170308_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 11, 46, 24, 121812, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 11, 46, 24, 121871, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
