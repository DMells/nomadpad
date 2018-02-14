# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0084_auto_20180202_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='./static/images'),
        ),
    ]