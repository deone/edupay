# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class EduPayUser(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(User)
    phone_number = models.CharField(_('phone number'), max_length=11)

class School(EduPayUser):
    name = models.CharField(_('name'), max_length=100)
    address = models.CharField(_('address'), max_length=255)
    name_of_head = models.CharField(_('name of school head'), max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(_('first name'), max_length=25)
    last_name = models.CharField(_('last name'), max_length=25)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

class PersonWithAddress(Person, EduPayUser):
    class Meta:
        abstract = True

    house_address = models.CharField(_('house address'), max_length=255)
    work_address = models.CharField(_('work address'), max_length=255)

class Parent(PersonWithAddress):
    pass

class Agent(PersonWithAddress):
    BANK_CHOICES = (
        ('', 'Choose...'),
        ('GTBank', 'GTBank'),
        ('UBA', 'UBA'),
        ('First Bank', 'First Bank'),
        ('Union Bank', 'Union Bank'),
        ('Ecobank', 'Ecobank'),
    )

    account_number = models.CharField(_('account number'), max_length=10)
    account_name = models.CharField(_('account name'), max_length=50)
    bank_name = models.CharField(_('bank name'), max_length=25, choices=BANK_CHOICES)

    def __str__(self):
        return self.get_full_name()

class Child(Person):
    parent = models.ForeignKey(Parent)
    school = models.ForeignKey(School)
    fee_per_term = models.CharField(_('fee per term'), max_length=20)

    def __str__(self):
        return self.get_full_name()