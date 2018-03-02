# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class School(models.Model):
    name = models.CharField(_('name'), max_length=50)
    address = models.CharField(_('address'), max_length=255)
    name_of_head = models.CharField(_('name of school head'), max_length=50)
    phone_number = models.CharField(_('phone number'), max_length=11)
    email = models.EmailField(_('email'))
    password = models.CharField(_('password'), max_length=128)

    def __str__(self):
        return self.name

""" class Parent(models.Model):
    pass

class Agent(models.Model):
    pass """