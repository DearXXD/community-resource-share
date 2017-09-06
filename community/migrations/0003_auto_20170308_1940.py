# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20170307_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': '\u793e\u533a', 'verbose_name_plural': '\u793e\u533a'},
        ),
        migrations.AlterField(
            model_name='community_statistical',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 11, 40, 40, 606366, tzinfo=utc)),
        ),
    ]
