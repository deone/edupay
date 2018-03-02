from django import forms

from models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'St. Alexis International School', 'class': 'form-control'})
        }