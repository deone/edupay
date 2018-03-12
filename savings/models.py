# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class DateCreated(models.Model):
    class Meta:
        abstract = True

    date_created = models.DateTimeField(default=timezone.now)

class EduPayUser(DateCreated):
    class Meta:
        abstract = True

    user = models.OneToOneField(User)

class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(_('first name'), max_length=25)
    last_name = models.CharField(_('last name'), max_length=25)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()

class PersonWithAddress(Person, EduPayUser):
    class Meta:
        abstract = True

    house_address = models.CharField(_('house address'), max_length=255)
    work_address = models.CharField(_('work address'), max_length=255)

class School(EduPayUser):
    name = models.CharField(_('name'), max_length=100)
    address = models.CharField(_('address'), max_length=255)
    name_of_head = models.CharField(_('name of school head'), max_length=50)

    def __str__(self):
        return self.name

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

class Child(Person, DateCreated):
    parent = models.ForeignKey(Parent)
    school = models.ForeignKey(School)
    fee_per_term = models.CharField(_('fee per term'), max_length=20)

class SavingPlan(DateCreated):
    FREQUENCY_CHOICES = (
        ('', 'Choose...'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )

    TERM_CHOICES = (
        ('', 'Choose...'),
        ('1', '1st Term - Sep. 20'),
        ('2', '2nd Term - Jan. 10'),
        ('3', '3rd Term - Apr. 15'),
    )

    PAYMENT_MODE_CHOICES = (
        ('', 'Choose...'),
        ('agent', 'Agent'),
        ('direct debit', 'Direct debit'),
    )

    parent = models.ForeignKey(Parent)
    total_fee = models.IntegerField()
    amount_to_be_saved = models.IntegerField()
    frequency = models.CharField(max_length=7, choices=FREQUENCY_CHOICES)
    target_term = models.CharField(max_length=1, choices=TERM_CHOICES)
    target_date = models.DateField()
    contribution = models.PositiveSmallIntegerField()
    mode_of_payment = models.CharField(max_length=15, choices=PAYMENT_MODE_CHOICES)
    is_active = models.BooleanField(default=True)

class Saving(DateCreated):
    saving_plan = models.ForeignKey(SavingPlan)