from .models import *
from core.admin import techrahis_admin

techrahis_admin.register(BlogCategory)
techrahis_admin.register(Tag)
techrahis_admin.register(Blog)