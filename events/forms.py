from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# create a event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields = "__all__"
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')

        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Event'}),
            # 'event_date': forms.TextInput(attrs={'type': 'datetime-local'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Name of Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


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
