# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_parameter_file_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='help',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
