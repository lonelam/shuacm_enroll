# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acmer',
            name='id',
        ),
        migrations.AlterField(
            model_name='acmer',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='acmer',
            name='stuno',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
