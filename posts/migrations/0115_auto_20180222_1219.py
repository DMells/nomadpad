# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-22 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0114_auto_20180222_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
    ]
