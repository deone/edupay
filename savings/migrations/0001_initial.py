# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('address', models.TextField(verbose_name='address')),
                ('name_of_head', models.CharField(max_length=50, verbose_name='name of school head')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
            ],
        ),
    ]