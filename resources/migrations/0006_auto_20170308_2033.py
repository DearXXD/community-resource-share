# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20170308_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': '\u8d44\u6e90', 'verbose_name_plural': '\u8d44\u6e90'},
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resource_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 12, 33, 21, 833530, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 12, 33, 21, 833607, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
