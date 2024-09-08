import os
import hashlib
from django.db import models
from django.core.files.storage import FileSystemStorage

def get_unique_file_name(instance, filename):
    # Generate a unique hash using the original filename and a random string
    hash_object = hashlib.md5(filename.encode())
    unique_filename = f"{hash_object.hexdigest()}_{filename}"
    return os.path.join('relevant_files/', unique_filename)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class HireRequest(models.Model):
    OPPORTUNITY_CHOICES = [
        ('freelance', 'Freelance'),
        ('part_time', 'Part-Time'),
        ('full_time', 'Full-Time'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    opportunity_type = models.CharField(max_length=20, choices=OPPORTUNITY_CHOICES)
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_description = models.TextField()
    skills_required = models.TextField(blank=True, null=True)
    project_scope = models.TextField(blank=True, null=True)  # For freelance
    estimated_duration = models.CharField(max_length=50, blank=True, null=True)  # For freelance
    budget = models.CharField(max_length=50, blank=True, null=True)  # For freelance
    location = models.CharField(max_length=255, blank=True, null=True)  # For full-time
    salary_range = models.CharField(max_length=50, blank=True, null=True)  # For full-time
    benefits = models.TextField(blank=True, null=True)  # For full-time
    desired_start_date = models.DateField()
    how_heard = models.CharField(max_length=255, blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    relevant_file = models.FileField(upload_to=get_unique_file_name, blank=True, null=True)  # For freelance and full-time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.job_title}'
