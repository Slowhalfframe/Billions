# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20190428_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='logo_content',
            field=models.CharField(max_length=12, null=True, verbose_name='网站标题'),
        ),
    ]
