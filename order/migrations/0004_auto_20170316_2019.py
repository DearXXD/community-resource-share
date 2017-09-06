# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20170316_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='begin_time',
            field=models.DateField(default=datetime.datetime(2017, 3, 16, 12, 19, 23, 952399, tzinfo=utc), verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(unique=True, max_length=25, verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]
