# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20170309_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='begin_time',
            field=models.DateField(default=datetime.datetime(2017, 3, 16, 12, 17, 1, 714222, tzinfo=utc), verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='order',
            name='intergration',
            field=models.IntegerField(verbose_name='\u79ef\u5206'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='\u8ba2\u5355\u53f7'),
        ),
        migrations.AlterField(
            model_name='order',
            name='process',
            field=models.IntegerField(default=1, verbose_name='\u8fdb\u7a0b', choices=[(1, b'\xe9\x94\x81\xe5\xae\x9a\xe4\xbd\xbf\xe7\x94\xa8'), (2, b'\xe5\x8f\x96\xe6\xb6\x88\xe9\x94\x81\xe5\xae\x9a'), (3, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (4, b'\xe5\xbd\x92\xe8\xbf\x98')]),
        ),
    ]
