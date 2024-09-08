from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='project_covers/')
    short_description = models.TextField(help_text="Short description for listing page")
    long_description = models.TextField(help_text="Long description for detail page")
    technologies = models.TextField(help_text="Comma-separated list of technologies")
    live_demo_url = models.URLField(blank=True, null=True)
    source_code_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title