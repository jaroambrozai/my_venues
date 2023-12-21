from django import forms
from django.forms import ModelForm
from .models import Venue


# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = "__all__"
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Venue'} ),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone #'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
