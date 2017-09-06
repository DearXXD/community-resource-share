# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20170308_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_statistical',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 9, 5, 24, 43, 180697, tzinfo=utc)),
        ),
    ]
