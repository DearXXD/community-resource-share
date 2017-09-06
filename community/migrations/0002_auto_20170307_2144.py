# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='community_license',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8bc1\u4ef6\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='community_statistical',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 7, 13, 44, 7, 547011, tzinfo=utc)),
        ),
    ]
