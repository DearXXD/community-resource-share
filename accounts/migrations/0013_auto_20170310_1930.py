# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170307_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='facade_id_card',
        ),
        migrations.RemoveField(
            model_name='user',
            name='living_proof',
        ),
        migrations.RemoveField(
            model_name='user',
            name='obverse_id_card',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 10, 11, 30, 26, 994992, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 10, 11, 30, 26, 995613, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4'),
        ),
    ]
