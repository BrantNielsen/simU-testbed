# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-21 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('value_hash', models.BinaryField(db_index=True)),
            ],
        ),
    ]
