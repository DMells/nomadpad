# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-27 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0120_auto_20180227_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='editedimage',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='primary_images'),
        ),
    ]
