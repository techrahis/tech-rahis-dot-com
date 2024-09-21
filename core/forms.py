from django.core.exceptions import ValidationError
from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean(self):
        cleaned_data = super().clean()
        # Custom validation can be added here if needed
        return cleaned_data
    
class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['name', 'email', 'phone', 'website', 'preferred_date', 'preferred_time']

    def clean(self):
        cleaned_data = super().clean()
        # Custom validation can be added here if needed
        return cleaned_data