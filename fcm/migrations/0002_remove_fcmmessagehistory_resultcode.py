# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fcmmessagehistory',
            name='resultCode',
        ),
    ]