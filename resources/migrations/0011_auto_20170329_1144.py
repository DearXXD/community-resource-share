# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20170329_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.ImageField(upload_to=b'resource_picture/%Y/%m/%d', verbose_name='\u7269\u54c1\u7167\u7247')),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 29, 3, 44, 33, 843088, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='use_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 3, 3, 44, 33, 843153, tzinfo=utc), null=True, verbose_name='\u4f7f\u7528\u671f\u9650', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='pic',
            field=models.ManyToManyField(to='resources.Respic', null=True, blank=True),
        ),
    ]
