# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-09 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_parentslug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='catSlug',
        ),
    ]
