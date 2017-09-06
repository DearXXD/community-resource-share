# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170310_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=accounts.fields.ListField(default=[], max_length=100, verbose_name='\u8d2d\u7269\u8f66'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 16, 12, 54, 41, 635975, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 16, 12, 54, 41, 636306, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
    ]
