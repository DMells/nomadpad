# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-02 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0086_auto_20180202_1246'),
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
            field=models.FileField(null=True, upload_to='./static/images'),
        ),
    ]
