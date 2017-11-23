# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20171121_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]