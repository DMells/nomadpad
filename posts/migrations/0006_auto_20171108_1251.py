# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20171108_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_tag',
        ),
        migrations.AddField(
            model_name='post',
            name='category_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category'),
        ),
    ]