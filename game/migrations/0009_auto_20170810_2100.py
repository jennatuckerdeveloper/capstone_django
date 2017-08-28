# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_game_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='status',
        ),
        migrations.AddField(
            model_name='inventory',
            name='status',
            field=models.CharField(default='active', max_length=200),
        ),
    ]
