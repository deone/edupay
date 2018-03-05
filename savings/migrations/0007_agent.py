# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0006_auto_20180303_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('house_address', models.CharField(max_length=255, verbose_name='house address')),
                ('work_address', models.CharField(max_length=255, verbose_name='work address')),
                ('account_number', models.CharField(max_length=10, verbose_name='account number')),
                ('bank_name', models.CharField(max_length=50, verbose_name='bank name')),
            ],
        ),
    ]
