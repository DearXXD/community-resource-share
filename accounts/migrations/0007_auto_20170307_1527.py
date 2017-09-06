# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170307_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 7, 27, 27, 224558, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 7, 27, 27, 225141, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
    ]
