# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-28 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housetype', '0002_hotel_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='pic',
            field=models.ImageField(null=True, upload_to='static/housetype/img/', verbose_name='展示图'),
        ),
    ]
