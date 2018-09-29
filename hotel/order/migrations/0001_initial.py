# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-29 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MechantOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=50, verbose_name='订单号')),
                ('ordermessage', models.CharField(max_length=300, verbose_name='订单信息')),
            ],
        ),
    ]
