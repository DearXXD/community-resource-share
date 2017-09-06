# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=22, verbose_name='v\u79f0\u547c')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('content', models.TextField(verbose_name='\u610f\u89c1\u53cd\u9988')),
                ('is_replay', models.TextField(verbose_name='\u662f\u5426\u56de\u8bbf')),
                ('remind', models.TextField(verbose_name='\u5904\u7406\u8bb0\u5f55')),
            ],
        ),
    ]
