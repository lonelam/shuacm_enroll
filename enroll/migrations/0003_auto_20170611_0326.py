# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]