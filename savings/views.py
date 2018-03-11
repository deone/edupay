# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from models import Agent, Parent, Child
from forms import SchoolForm, AgentForm, ParentForm, AddChildForm

def login_redirect(request):
    username, password = request.POST['phone_number'], request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return login_redirect(request)
    else:
        form = SchoolForm(label_suffix='')
    return render(request, 'savings/school_form.html', {'form': form})

def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return login_redirect(request)
    else:
        form = ParentForm(label_suffix='')
    return render(request, 'savings/parent_form.html', {'form': form})

def create_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return login_redirect(request)
    else:
        form = AgentForm(label_suffix='')
    return render(request, 'savings/agent_form.html', {'form': form})

@login_required
def dashboard(request):
    context = {}
    if hasattr(request.user, 'parent'):
        parent = Parent.objects.get(user=request.user)
        if request.method == 'POST':
            form = AddChildForm(request.POST, parent=parent)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = AddChildForm(label_suffix='', parent=parent)
    
        context.update({'children': Child.objects.filter(parent=parent), 'form': form})

    return render(request, 'savings/dashboard.html', context)