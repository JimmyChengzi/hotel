# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-10 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_roomtype_isshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='库存'),
        ),
    ]
