# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20171117_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
    ]
