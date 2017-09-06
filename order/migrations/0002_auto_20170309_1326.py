# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='begin_time',
            field=models.DateField(default=datetime.datetime(2017, 3, 9, 5, 26, 3, 190388, tzinfo=utc), verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='order',
            name='process',
            field=models.IntegerField(default=2, verbose_name='\u8fdb\u7a0b', choices=[(1, b'\xe9\x94\x81\xe5\xae\x9a\xe4\xbd\xbf\xe7\x94\xa8'), (2, b'\xe5\x8f\x96\xe6\xb6\x88\xe9\x94\x81\xe5\xae\x9a'), (3, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (4, b'\xe5\xbd\x92\xe8\xbf\x98')]),
        ),
    ]
