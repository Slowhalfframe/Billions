# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_auto_20190428_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='logo_link',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='网站logo链接'),
        ),
        migrations.AlterField(
            model_name='topbox',
            name='content',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='顶部通告'),
        ),
    ]
