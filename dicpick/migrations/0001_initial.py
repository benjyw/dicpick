# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 23:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(max_length=10, unique=True)),
                ('admin_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.Group')),
                ('member_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(help_text='E.g., "Burning Man 2016".', max_length=40)),
                ('slug', models.SlugField(help_text='A short string to use in URLs.  E.g., "2016".', max_length=10)),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='dicpick.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('initial_score', models.IntegerField(blank=True, default=0)),
                ('do_not_assign_with', models.ManyToManyField(blank=True, related_name='_participant_do_not_assign_with_+', to='dicpick.Participant')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='dicpick.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='dicpick.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('num_people', models.IntegerField()),
                ('score', models.IntegerField()),
                ('assignees', models.ManyToManyField(blank=True, related_name='tasks', to='dicpick.Participant')),
                ('tags', models.ManyToManyField(blank=True, related_name='tasks', to='dicpick.Tag')),
            ],
            options={
                'ordering': ['task_type__name', 'date'],
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=40)),
                ('num_people', models.IntegerField()),
                ('score', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_types', to='dicpick.Event')),
                ('tags', models.ManyToManyField(blank=True, related_name='task_types', to='dicpick.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='dicpick.TaskType'),
        ),
        migrations.AddField(
            model_name='participant',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='participants', to='dicpick.Tag'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tasktype',
            unique_together=set([('event', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('task_type', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('event', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('event', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('camp', 'slug'), ('camp', 'name')]),
        ),
    ]
