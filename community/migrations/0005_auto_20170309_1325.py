# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20170309_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_statistical',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 9, 5, 25, 9, 855381, tzinfo=utc)),
        ),
    ]
