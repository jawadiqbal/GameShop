# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20160522_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='keys',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='keys_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
