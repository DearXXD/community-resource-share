# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('areacode', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u5e02',
                'verbose_name_plural': '\u5e02',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25, verbose_name='\u793e\u533a\u540d')),
                ('address', models.CharField(max_length=35, verbose_name='\u5730\u5740')),
                ('status', models.IntegerField(default=3, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u51bb\u7ed3'), (2, '\u5220\u9664'), (3, '\u5f85\u5ba1\u6838'), (4, '\u901a\u8fc7\u5ba1\u6838'), (5, '\u62d2\u7edd\u5ba1\u6838')])),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('phone', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('join_time', models.DateTimeField(auto_now=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('seal', models.ImageField(upload_to=b'community/seal/%Y/%m/%d', null=True, verbose_name='\u516c\u7ae0', blank=True)),
                ('community_license_img', models.ImageField(upload_to=b'community/license/%Y/%m/%d', null=True, verbose_name='\u76f8\u5173\u8bc1\u4ef6\u63cf\u4ef6', blank=True)),
                ('community_license', models.IntegerField(null=True, verbose_name='\u8bc1\u4ef6\u53f7', blank=True)),
                ('city', models.ForeignKey(blank=True, to='community.City', null=True)),
            ],
            options={
                'verbose_name': '\u793e\u533a\u7ba1\u7406',
                'verbose_name_plural': '\u793e\u533a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Community_Statistical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2017, 3, 7, 13, 43, 32, 250989, tzinfo=utc))),
                ('is_added', models.IntegerField(default=0)),
                ('is_deleted', models.IntegerField(default=0)),
                ('member', models.IntegerField(default=0)),
                ('community', models.ForeignKey(to='community.Community')),
            ],
            options={
                'verbose_name': '\u793e\u533a\u7edf\u8ba1',
                'verbose_name_plural': '\u793e\u533a\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('post_code', models.CharField(max_length=45, null=True, blank=True)),
                ('city', models.ForeignKey(to='community.City')),
            ],
            options={
                'verbose_name': '\u53bf',
                'verbose_name_plural': '\u53bf',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('orderid', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u7701\u4efd',
                'verbose_name_plural': '\u7701\u4efd',
            },
        ),
        migrations.AddField(
            model_name='community_statistical',
            name='province',
            field=models.ForeignKey(to='community.Province'),
        ),
        migrations.AddField(
            model_name='community',
            name='district',
            field=models.ForeignKey(blank=True, to='community.District', null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='manager',
            field=models.ForeignKey(related_name='community', verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(related_name='belong_to_community', null=True, verbose_name='\u6210\u5458', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='community',
            name='province',
            field=models.ForeignKey(blank=True, to='community.Province', null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(to='community.Province'),
        ),
    ]
