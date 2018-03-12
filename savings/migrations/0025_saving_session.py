# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_auto_20170916_2123'),
        ('savings', '0024_saving'),
    ]

    operations = [
        migrations.AddField(
            model_name='saving',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='session.Session'),
            preserve_default=False,
        ),
    ]
