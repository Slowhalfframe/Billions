# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('logo_src', models.ImageField(upload_to='common/static/logo', verbose_name='LOGO图片地址')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
    ]
