# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dicpick', '0002_task_do_not_assign_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automatic', models.BooleanField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicpick.Participant')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignees',
        ),
        migrations.AddField(
            model_name='assignment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicpick.Task'),
        ),
    ]
