# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20160520_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='title',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Casual', 'Casual'), ('FPS', 'FPS'), ('Indie', 'Indie'), ('Multiplayer', 'Multiplayer'), ('RPG', 'RPG'), ('Racing', 'Racing'), ('Simulation', 'Simulation'), ('Sports', 'Sports'), ('Strategy', 'Strategy')], max_length=120),
        ),
    ]
