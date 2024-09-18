import os
import uuid
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import date

def unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('blog_thumbnails/', filename)

def unique_cover_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('blog_covers/', filename)

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Tag Name"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False, blank=False, verbose_name=_("Title"))
    thumbnail = models.ImageField(upload_to=unique_filename, verbose_name=_("Thumbnail"))
    cover_image = models.ImageField(upload_to=unique_cover_filename, verbose_name=_("Cover Image"))
    slug = models.SlugField(unique=True, null=False, blank=False, verbose_name=_("Slug"))
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name=_("Category"))
    short_description = models.TextField(help_text=_("Short description for listing page"), verbose_name=_("Short Description"))
    long_description = models.TextField(help_text=_("Long description in markdown format"), verbose_name=_("Long Description"))
    date = models.DateField(default=date.today, help_text=_("Date when the blog was completed"), verbose_name=_("Date"))
    tags = models.ManyToManyField(Tag, help_text=_("List of tags"), verbose_name=_("Tags"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            for x in range(1, 1000):
                if not Blog.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{original_slug}-{x}"
        super(Blog, self).save(*args, **kwargs)