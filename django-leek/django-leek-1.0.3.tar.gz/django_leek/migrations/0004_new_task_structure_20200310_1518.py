# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-10 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_leek', '0003_auto_20180910_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickled_task', models.BinaryField(max_length=4096)),
                ('pool', models.CharField(max_length=256, null=True)),
                ('queued_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('pickled_exception', models.BinaryField(max_length=2048, null=True)),
                ('pickled_return', models.BinaryField(max_length=4096, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FailedTasks',
        ),
        migrations.DeleteModel(
            name='QueuedTasks',
        ),
        migrations.DeleteModel(
            name='SuccessTasks',
        ),
    ]
