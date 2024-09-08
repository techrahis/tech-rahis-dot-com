from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class TechRahisAdmin(admin.AdminSite):
    site_header = 'TechRahis Admin'
    site_title = 'TechRahis Admin'


techrahis_admin = TechRahisAdmin(name='techrahis_admin')

techrahis_admin.register(User)
techrahis_admin.register(Contact)
techrahis_admin.register(HireRequest)
