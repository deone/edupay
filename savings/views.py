# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login

from forms import SchoolForm, AgentForm
from models import Agent

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            username, password = request.POST['phone_number'], request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = SchoolForm(label_suffix='')
    return render(request, 'savings/school_form.html', {'form': form})

# def create_parent(request):
    # return render(request, 'savings/parent_form.html', {'form': form})

class AgentCreate(CreateView):
    model = Agent
    form_class = AgentForm
    success_url = '/agent/new'