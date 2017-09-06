# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20170308_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='resources',
        ),
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ManyToManyField(related_name='resources', null=True, verbose_name='\u7c7b\u522b', to='resources.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 13, 2, 2, 833183, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 13, 2, 2, 833253, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
