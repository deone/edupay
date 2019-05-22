# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Agent, Parent, Child, SavingPlan, Saving
from .forms import SchoolForm, AgentForm, ParentForm, AddChildForm, SavingPlanForm

def get_parent(user):
    return Parent.objects.get(user=user)

def login_redirect(request):
    username, password = request.POST['phone_number'], request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            return login_redirect(request)
    else:
        form = SchoolForm(label_suffix='')
    return render(request, 'savings/school_form.html', {'form': form})

def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            return login_redirect(request)
    else:
        form = ParentForm(label_suffix='')
    return render(request, 'savings/parent_form.html', {'form': form})

def create_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST, label_suffix='')
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
        parent = get_parent(request.user)
        if request.method == 'POST':
            form = AddChildForm(request.POST, parent=parent)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = AddChildForm(label_suffix='', parent=parent)
    
        context.update({'children': Child.objects.filter(parent=parent), 'form': form})
    return render(request, 'savings/dashboard.html', context)

# @must_be_parent
@login_required
def savings(request):
    context = {}
    parent = get_parent(request.user)
    total_fee = parent.child_set.all().aggregate(Sum('fee_per_term'))['fee_per_term__sum'] or 0
    amount_to_be_saved = (settings.SAVINGS_PERCENT / 100) * total_fee

    if request.method == 'POST':
        form = SavingPlanForm(request.POST, parent=parent)
        if form.is_valid():
            form.save()
            return redirect('savings')
    else:
        form = SavingPlanForm(label_suffix='', parent=parent, initial={
            'total_fee': total_fee, 'amount_to_be_saved': amount_to_be_saved})

    saving_plans = SavingPlan.objects.filter(parent=parent)
    context.update({
        'form': form,
        'savings_percent': settings.SAVINGS_PERCENT,
        'saving_plans': saving_plans
    })
    return render(request, 'savings/savings.html', context)

@api_view(['GET'])
def request_parent(request):
    # <QueryDict: {u'phone_number': [u'08029299274']}>
    phone_number = request.GET.get('phone_number')
    if phone_number != None:
        try:
            user = User.objects.get(username=phone_number)
        except User.DoesNotExist:
            return Response({'error': 'Phone number not found'})

        try:
            parent = user.parent
        except:
            return Response({'error': 'Phone number does not belong to parent'})

        return Response({
            'phone_number': phone_number,
            'name': parent.get_full_name(),
            'contribution_amount': parent.savingplan_set.all()[0].contribution
        })

    return Response({'error': 'Parameter not found'})

@api_view(['POST'])
def record_payment(request):
    # <QueryDict: {u'phone_number': [u'08022334455'], u'amount': [u'500']}>
    phone_number = request.POST.get('phone_number')
    amount = request.POST.get('amount')
    if phone_number != None:
        parent = User.objects.get(username=phone_number).parent
        saving_plan = SavingPlan.objects.filter(parent=parent)[0]
        Saving.objects.create(
            saving_plan=saving_plan,
            amount=amount
            )
        return Response({'success': 'Payment recorded'})
    
    return Response({'error': 'Parameter not found'})
