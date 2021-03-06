# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('savings', '0010_auto_20180305_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone number')),
                ('first_name', models.CharField(max_length=25, verbose_name='first name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last name')),
                ('house_address', models.CharField(max_length=255, verbose_name='house address')),
                ('work_address', models.CharField(max_length=255, verbose_name='work address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(default='08022334455', max_length=11, verbose_name='phone number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
