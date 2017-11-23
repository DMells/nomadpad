# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20171115_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Category'),
        ),
    ]