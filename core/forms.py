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



class HireRequestForm(forms.ModelForm):
    OPPORTUNITY_CHOICES = [
        ('freelance', 'Freelance'),
        ('part_time', 'Part-Time'),
        ('full_time', 'Full-Time'),
    ]

    class Meta:
        model = HireRequest
        fields = [
            'name', 'email', 'phone_number', 'opportunity_type', 'job_title',
            'company_name', 'job_description', 'skills_required', 'project_scope',
            'estimated_duration', 'budget', 'location', 'salary_range', 'benefits',
            'desired_start_date', 'how_heard', 'additional_comments', 'relevant_file'
        ]
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4}),
            'skills_required': forms.Textarea(attrs={'rows': 2}),
            'project_scope': forms.Textarea(attrs={'rows': 2}),
            'estimated_duration': forms.TextInput(attrs={'placeholder': 'e.g., 3 months'}),
            'budget': forms.TextInput(attrs={'placeholder': 'e.g., $5000'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., New York'}),
            'salary_range': forms.TextInput(attrs={'placeholder': 'e.g., $60,000 - $80,000'}),
            'benefits': forms.Textarea(attrs={'rows': 2}),
            'desired_start_date': forms.DateInput(attrs={'type': 'date'}),
            'how_heard': forms.TextInput(attrs={'placeholder': 'e.g., Referral, Job Board'}),
            'additional_comments': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_relevant_file(self):
        relevant_file = self.cleaned_data.get('relevant_file')
        if relevant_file:
            if relevant_file.size > 10 * 1024 * 1024:  # 10MB limit
                raise ValidationError("The file size should not exceed 10MB.")
        return relevant_file
