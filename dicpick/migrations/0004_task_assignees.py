# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicpick', '0003_auto_20160810_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignees',
            field=models.ManyToManyField(blank=True, related_name='tasks', through='dicpick.Assignment', to='dicpick.Participant'),
        ),
    ]