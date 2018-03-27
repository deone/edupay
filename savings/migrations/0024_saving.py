# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0023_savingplan_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('saving_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.SavingPlan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]