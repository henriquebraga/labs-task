# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161126_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('full_name',), 'verbose_name': 'employee', 'verbose_name_plural': 'employees'},
        ),
    ]