# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0022_savingplan_mode_of_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingplan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
