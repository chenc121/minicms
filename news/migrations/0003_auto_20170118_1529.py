# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170112_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='pbulished',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=256, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, verbose_name='栏目地址'),
        ),
    ]
