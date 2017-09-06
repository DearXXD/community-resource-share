# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='\u7269\u54c1\u540d\u79f0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 11, 41, 22, 148501, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 11, 41, 22, 148563, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
