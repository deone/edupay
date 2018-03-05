# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from forms import SchoolForm
from models import Agent

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/school/new')
    else:
        form = SchoolForm(label_suffix='')
    return render(request, 'savings/school_form.html', {'form': form})

# def create_parent(request):
    # return render(request, 'savings/parent_form.html', {'form': form})

class AgentCreate(CreateView):
    model = Agent
    fields = '__all__'
    success_url = '/agent/new'