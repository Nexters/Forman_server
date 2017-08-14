# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '그룹', 'verbose_name_plural': '그룹'},
        ),
        migrations.AlterModelOptions(
            name='groupusers',
            options={'verbose_name': '그룹 User', 'verbose_name_plural': '그룹 User'},
        ),
        migrations.AlterModelOptions(
            name='routine',
            options={'verbose_name': '경로', 'verbose_name_plural': '경로'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': '일정', 'verbose_name_plural': '일정'},
        ),
        migrations.AlterField(
            model_name='schedule',
            name='object',
            field=models.SmallIntegerField(choices=[(1, 'Business'), (0, 'Personal')], verbose_name='목적'),
        ),
    ]
