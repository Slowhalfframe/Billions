# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20190426_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopBox',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=256, verbose_name='顶部通告')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '顶部通告',
                'verbose_name_plural': '顶部通告',
            },
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'LOGO', 'verbose_name_plural': 'LOGO'},
        ),
        migrations.AlterModelOptions(
            name='nav',
            options={'verbose_name': '导航', 'verbose_name_plural': '导航'},
        ),
    ]