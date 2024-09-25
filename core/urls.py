from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .admin import techrahis_admin

urlpatterns = [
    path('admin/', techrahis_admin.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('faq/', views.faq, name='faq'),
    path("not-found/", views.not_found_page, name="not_found_page"),
    path("get-free-consultation/", views.get_free_consultation, name="get_free_consultation"),
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)