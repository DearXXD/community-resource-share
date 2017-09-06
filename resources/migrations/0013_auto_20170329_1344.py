# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20170329_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='pic',
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 5, 44, 4, 426181, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='\u7269\u54c1\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 5, 44, 4, 426244, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
    ]
