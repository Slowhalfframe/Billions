# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logo_src',
            field=models.ImageField(upload_to='static/common/logo', verbose_name='LOGO图片地址'),
        ),
    ]
