from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from models import School, Agent, Parent

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
        school = School.objects.create(
            user=user, phone_number=phone_number, name_of_head=name_of_head, address=address, name=name)

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'house_address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'House 5, B Close, Festac Town'
            }),
            'work_address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '3, Broad Street, Marina'
            }),
            'account_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'bank_name': forms.Select(attrs={
                'class': 'custom-select d-block w-100'
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

class ParentForm(CreateBaseForm):
    first_name = forms.CharField(label=_('First name'), max_length=25, widget=forms.TextInput(attrs={
                'class': 'form-control'
            }))
    last_name = forms.CharField(label=_('Last name'), max_length=25, widget=forms.TextInput(attrs={
                'class': 'form-control'
            }))
    house_address = forms.CharField(label=_('House address'), max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'House 5, B Close, Festac Town'
            }))
    work_address = forms.CharField(label=_('Work address'), max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '3, Broad Street, Marina'
            }))

    def save(self):
        data = self.cleaned_data
        first_name, last_name = data['first_name'], data['last_name']
        email, password = data.get('email', None), data['password']
        house_address, work_address = data['house_address'], data['work_address']
        phone_number = '0' + str(data['phone_number'])

        user = User.objects.create_user(phone_number, email, password)
        parent = Parent.objects.create(
            user=user, first_name=first_name, last_name=last_name,
            house_address=house_address, work_address=work_address)