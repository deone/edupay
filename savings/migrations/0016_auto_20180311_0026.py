# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0015_child_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='school',
            name='phone_number',
        ),
    ]