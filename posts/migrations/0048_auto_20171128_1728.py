# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0047_auto_20171128_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
    ]
