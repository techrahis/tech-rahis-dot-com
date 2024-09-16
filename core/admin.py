from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class TechRahisAdmin(admin.AdminSite):
    site_header = 'TechRahis Admin'
    site_title = 'TechRahis Admin'


techrahis_admin = TechRahisAdmin(name='techrahis_admin')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'message', 'created_at')
    readonly_fields = ('created_at',)

    def title(self, obj):
        return f"{obj.name} - {obj.subject}"
    title.short_description = 'Title'

techrahis_admin.register(Contact, ContactAdmin)
techrahis_admin.register(User)
techrahis_admin.register(HireRequest)
