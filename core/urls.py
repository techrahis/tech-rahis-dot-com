from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .admin import techrahis_admin

urlpatterns = [
    path('admin/', techrahis_admin.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('others/', views.others, name='others'),
    path('hire-me/', views.hire_me, name='hire_me'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('colophon/', views.colophon, name='colophon'),
    path("not-found/", views.not_found_page, name="not_found_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)