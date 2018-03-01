# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView

from models import School

class SchoolCreate(CreateView):
    model = School
    fields = ['name', 'address', 'name_of_head', 'phone_number', 'email', 'password']