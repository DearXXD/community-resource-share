# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170307_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='\u7ba1\u7406\u5458'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 6, 59, 21, 865384, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 6, 59, 21, 865841, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
    ]
