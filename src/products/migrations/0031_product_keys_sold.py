# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20160523_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keys_sold',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
