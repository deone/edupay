from django import forms
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import School, Agent, Parent, Child, SavingPlan

from datetime import datetime

class CreateBaseForm(forms.Form):
    phone_number = forms.IntegerField(label=_('Phone number'), widget=forms.NumberInput(attrs={
                'placeholder': '07033445566',
                'class': 'form-control'
            }))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'form-control'
            }), required=False)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={
                'class': 'form-control'
            }))

    def clean(self):
        cleaned_data = super(CreateBaseForm, self).clean()
        email = cleaned_data.get('email')
        phone_number = '0' + str(cleaned_data.get('phone_number'))
        password = cleaned_data.get('password')

        try:
            user = User.objects.create_user(phone_number, email, password)
        except IntegrityError:
            raise forms.ValidationError("Phone number already exists.")
        else:
            cleaned_data.update({'user': user})

        return cleaned_data

class SchoolForm(CreateBaseForm):
    name = forms.CharField(label=_('School name'), max_length=50, widget=forms.TextInput(attrs={
                'placeholder': 'St. Alexis International School',
                'class': 'form-control'
            }))
    address = forms.CharField(label=_('Address'), max_length=255, widget=forms.TextInput(attrs={
                'placeholder': '12 Main St, Ebute-Metta',
                'class': 'form-control'
            }))
    name_of_head = forms.CharField(label=_('Name of school head'), max_length=50, widget=forms.TextInput(attrs={
                'placeholder': 'Seyi Chukwuka',
                'class': 'form-control'
            }))

    def save(self):
        data = self.cleaned_data
        del data['password'], data['email'], data['phone_number']
        School.objects.create(**data)

class PersonForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=25, widget=forms.TextInput(attrs={
                'class': 'form-control'
            }))
    last_name = forms.CharField(label=_('Last name'), max_length=25, widget=forms.TextInput(attrs={
                'class': 'form-control'
            }))

class PersonWithAddressForm(PersonForm):
    house_address = forms.CharField(label=_('House address'), max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'House 5, B Close, Festac Town'
            }))
    work_address = forms.CharField(label=_('Work address'), max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '3, Broad Street, Marina'
            }))

class AgentForm(CreateBaseForm, PersonWithAddressForm):
    BANK_CHOICES = (
        ('', 'Choose...'),
        ('GTBank', 'GTBank'),
        ('UBA', 'UBA'),
        ('First Bank', 'First Bank'),
        ('Union Bank', 'Union Bank'),
        ('Ecobank', 'Ecobank'),
    )
    account_name = forms.CharField(label=_('Account name'), max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    bank_name = forms.ChoiceField(label=_('Bank name'), choices=BANK_CHOICES, widget=forms.Select(
        attrs={'class': 'custom-select d-block w-100'}))
    account_number = forms.CharField(label=_('Account number'), max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    def save(self):
        data = self.cleaned_data
        del data['email'], data['password'], data['phone_number']
        Agent.objects.create(**data)

class ParentForm(CreateBaseForm, PersonWithAddressForm):
    def save(self):
        data = self.cleaned_data
        del data['email'], data['password'], data['phone_number']
        Parent.objects.create(**data)

class AddChildForm(PersonForm):
    def __init__(self, *args, **kwargs):
        self.parent = kwargs.pop('parent')
        super(AddChildForm, self).__init__(*args, **kwargs)

    school = forms.ModelChoiceField(label=_('School'), queryset=School.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}), empty_label='Choose...')
    fee_per_term = forms.IntegerField(label=_('Fee per term'), widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    def save(self):
        data = self.cleaned_data
        data.update({'parent': self.parent})
        Child.objects.create(**data)

class SavingPlanForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.parent = kwargs.pop('parent')
        super(SavingPlanForm, self).__init__(*args, **kwargs)

    total_fee = forms.IntegerField(label=_('Total fee'), widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': True}))
    amount_to_be_saved = forms.IntegerField(label=_('Amount to be saved'), widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': True}))
    frequency = forms.ChoiceField(label=_('Contribution Frequency'), choices=SavingPlan.FREQUENCY_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'onchange': 'computeContribution()'}))
    target_term = forms.ChoiceField(label=_('Target term'), choices=SavingPlan.TERM_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control', 'onchange': 'computeContribution()'}))
    target_date = forms.CharField(label=_('Target date'), widget=forms.TextInput(
        attrs={'class': 'form-control', 'readonly': True}))
    contribution = forms.IntegerField(label=_('Contribution'), widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': True}))
    mode_of_payment = forms.ChoiceField(label=_('Mode of payment'), choices=SavingPlan.PAYMENT_MODE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control'}))

    def save(self):
        data = self.cleaned_data
        text_date = data['target_date']
        data.update({
            'parent': self.parent,
            'target_date': datetime.strptime(text_date, '%b %d %Y')
        })
        SavingPlan.objects.create(**data)
