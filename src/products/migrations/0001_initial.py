# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to=products.models.upload_location)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.CharField(max_length=120)),
            ],
        ),
    ]