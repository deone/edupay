from django import forms

from models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'St. Alexis International School',
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': '12 Main St, Ebute-Metta',
                'class': 'form-control'
            }),
            'name_of_head': forms.TextInput(attrs={
                'placeholder': 'Seyi Chukwuka',
                'class': 'form-control'
            }),
            'phone_number': forms.NumberInput(attrs={
                'placeholder': '07033445566',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }