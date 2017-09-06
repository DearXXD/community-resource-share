# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=11, verbose_name='\u7528\u6237\u540d')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6fc0\u6d3b')),
                ('is_staff', models.BooleanField(default=True, verbose_name='\u7ba1\u7406\u5458f')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u7ba1\u7406\u5458')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2017, 3, 7, 6, 52, 2, 712840, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('email', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('status', models.IntegerField(default=2, verbose_name='\u72b6\u6001', choices=[(1, b'\xe5\x86\xbb\xe7\xbb\x93'), (2, b'\xe6\xad\xa3\xe5\xb8\xb8'), (3, b'\xe5\x88\xa0\xe9\x99\xa4')])),
                ('address', models.CharField(max_length=40, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('id_card', models.CharField(max_length=20, unique=True, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('facade_id_card', models.ImageField(upload_to=b'user/idcard/%Y/%m/%d', null=True, verbose_name='\u8eab\u4efd\u8bc1\u6b63\u9762', blank=True)),
                ('obverse_id_card', models.ImageField(upload_to=b'user/idcard/%Y/%m/%d', null=True, verbose_name='\u8eab\u4efd\u8bc1\u53cd\u9762', blank=True)),
                ('living_proof', models.ImageField(upload_to=b'user/living_proof/%Y/%m/%d', null=True, verbose_name='\u5c45\u4f4f\u8bc1\u660e', blank=True)),
                ('join_time', models.DateTimeField(default=datetime.datetime(2017, 3, 7, 6, 52, 2, 713311, tzinfo=utc), verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('type', models.IntegerField(default=1, verbose_name='\u7c7b\u578b', choices=[(1, b'\xe7\x94\xa8\xe6\x88\xb7'), (2, b'\xe7\xa4\xbe\xe5\x8c\xba\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98'), (3, b'\xe8\xb6\x85\xe7\xba\xa7\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')])),
                ('integration', models.IntegerField(default=500, verbose_name='\u4fe1\u7528\u79ef\u5206')),
                ('group', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
