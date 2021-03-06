# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0009_auto_20180305_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='bank_name',
            field=models.CharField(choices=[('', 'Choose...'), ('GTBank', 'GTBank'), ('UBA', 'UBA'), ('First Bank', 'First Bank'), ('Union Bank', 'Union Bank'), ('Ecobank', 'Ecobank')], max_length=25, verbose_name='bank name'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='last name'),
        ),
    ]
