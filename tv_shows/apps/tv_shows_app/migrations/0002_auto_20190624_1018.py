# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trips',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
