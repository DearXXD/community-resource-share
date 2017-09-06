# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20170309_1325'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0009_auto_20170309_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.PositiveIntegerField(unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('intergration', models.PositiveIntegerField(verbose_name='\u79ef\u5206')),
                ('is_complete', models.BooleanField(default=False, verbose_name='\u4ea4\u6362\u662f\u5426\u540e\u5b8c\u6210')),
                ('is_damage', models.BooleanField(default=False, verbose_name='\u662f\u5426\u635f\u574f')),
                ('damage_pic', models.ImageField(default=None, upload_to=b'order/damage/%Y/%m/%d', null=True, verbose_name='\u635f\u574f\u90e8\u5206\u7684\u7167\u7247', blank=True)),
                ('process', models.IntegerField(default=1, verbose_name='\u8fdb\u7a0b', choices=[(1, b'\xe9\x94\x81\xe5\xae\x9a\xe4\xbd\xbf\xe7\x94\xa8'), (2, b'\xe5\x8f\x96\xe6\xb6\x88\xe9\x94\x81\xe5\xae\x9a'), (3, b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (4, b'\xe5\xbd\x92\xe8\xbf\x98')])),
                ('begin_time', models.DateField(default=datetime.datetime(2017, 3, 9, 5, 25, 9, 869193, tzinfo=utc), verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateField(default=None, null=True, verbose_name='\u5b8c\u6210\u65f6\u95f4', blank=True)),
                ('buyer', models.ForeignKey(related_name='buyer_order', verbose_name='\u4f7f\u7528\u8005', to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(verbose_name='\u8ba2\u5355\u6240\u5c5e\u793e\u533a', to='community.Community')),
                ('master', models.ForeignKey(related_name='master_order', verbose_name='\u7269\u54c1\u6240\u5c5e\u4eba', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(related_name='order', verbose_name='\u8d44\u6e90', to='resources.Resource')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
    ]
