# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-10 08:59
from __future__ import unicode_literals
from django.db import migrations, models
import mptt.fields
import django.db.models.deletion
import django.utils.timezone
import mptt
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20180410_0943'),
    ]

    operations = [
	migrations.AddField(
		model_name="Post",
		name = "Category",
		field =  models.ForeignKey('Category', null=True, blank=True),
),
    ]
