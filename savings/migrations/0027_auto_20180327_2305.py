# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-27 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0026_auto_20180327_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saving',
            name='amount',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]