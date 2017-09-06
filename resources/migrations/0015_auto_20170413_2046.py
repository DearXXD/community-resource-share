# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_auto_20170329_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='pic',
            field=accounts.fields.ListField(default=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 12, 46, 37, 474799, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 12, 46, 37, 474857, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
