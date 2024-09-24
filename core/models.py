import os
import hashlib
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

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
    
class Consultation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SiteData(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    x_twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    revalidate = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and SiteData.objects.exists():
            raise ValidationError('There can be only one instance of SiteData.')
        return super(SiteData, self).save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    def __str__(self):
        return "Site Data"