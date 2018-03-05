# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class School(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('name'), max_length=100)
    address = models.CharField(_('address'), max_length=255)
    name_of_head = models.CharField(_('name of school head'), max_length=50)
    phone_number = models.CharField(_('phone number'), max_length=11)

    def __str__(self):
        return self.name

""" class Parent(models.Model):
    pass """

class Agent(models.Model):
    first_name = models.CharField(_('name'), max_length=25)
    last_name = models.CharField(_('name'), max_length=25)
    house_address = models.CharField(_('house address'), max_length=255)
    work_address = models.CharField(_('work address'), max_length=255)
    account_number = models.CharField(_('account number'), max_length=10)
    account_name = models.CharField(_('account name'), max_length=50)
    bank_name = models.CharField(_('bank name'), max_length=50)

    def __str__(self):
        return self.name