# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_product_add_keys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to=products.models.upload_location),
        ),
    ]
