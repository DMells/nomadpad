# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-23 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0120_auto_20180223_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
    ]