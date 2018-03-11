from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from models import School, Agent, Parent, Child

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
        password = data['password']
        email = data.get('email', None)
        phone_number, name_of_head = '0' + str(data['phone_number']), data['name_of_head']
        name, address = data['name'], data['address']

        user = User.objects.create_user(phone_number, email, password)
        School.objects.create(
            user=user, phone_number=phone_number, name_of_head=name_of_head, address=address, name=name)

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
        first_name, last_name = data['first_name'], data['last_name']
        email, password = data.get('email', None), data['password']
        house_address, work_address = data['house_address'], data['work_address']
        phone_number, account_number = '0' + str(data['phone_number']), data['account_number']
        account_name, bank_name = data['account_name'], data['bank_name']

        user = User.objects.create_user(phone_number, email, password)
        Agent.objects.create(
            user=user, first_name=first_name, last_name=last_name,
            house_address=house_address, work_address=work_address,
            account_name=account_name, account_number=account_number,
            bank_name=bank_name)

class ParentForm(CreateBaseForm, PersonWithAddressForm):
    def save(self):
        data = self.cleaned_data
        first_name, last_name = data['first_name'], data['last_name']
        email, password = data.get('email', None), data['password']
        house_address, work_address = data['house_address'], data['work_address']
        phone_number = '0' + str(data['phone_number'])

        user = User.objects.create_user(phone_number, email, password)
        Parent.objects.create(
            user=user, first_name=first_name, last_name=last_name,
            house_address=house_address, work_address=work_address)

class AddChildForm(PersonForm):
    def __init__(self, *args, **kwargs):
        self.parent= kwargs.pop('parent')
        super(AddChildForm, self).__init__(*args, **kwargs)

    school = forms.ModelChoiceField(label=_('School'), queryset=School.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}), empty_label='Choose...')
    fee_per_term = forms.CharField(label=_('Fee per term'), max_length=20, widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    def save(self):
        # {'first_name': u'Ade', 'last_name': u'Ola', 'school': <School: St. James High School>, 'fee_per_term': u'20000'}
        data = self.cleaned_data
        data.update({'parent': self.parent})
        Child.objects.create(**self.cleaned_data)