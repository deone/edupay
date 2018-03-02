# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView

from forms import SchoolForm

class SchoolCreate(CreateView):
    form_class = SchoolForm
    template_name = 'savings/school_form.html'
    success_url = '/school/new'