# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0008_auto_20190507_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='EventDetails',
        ),
    ]
