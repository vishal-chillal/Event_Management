# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0009_auto_20190507_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createdevents',
            name='id',
        ),
        migrations.AlterField(
            model_name='createdevents',
            name='event_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='event_management.EventDetails'),
        ),
    ]
