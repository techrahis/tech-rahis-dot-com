from django.shortcuts import render
from .forms import *
from portfolios.models import Portfolio
from helpers.cache.page_cache import cache_if_not_debug

@cache_if_not_debug(60 * 60 * 15) # Cache for 15 minutes
def home(request):
    portfolios = Portfolio.objects.filter(featured=True).only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
    return render(request, 'home.html', {'portfolios': portfolios})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def not_found_page(request):
    return render(request, '404.html')

def contact(request):
    success_message = None
    error_message = None
    form_errors = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = "Your message has been sent successfully!"
                form = ContactForm()  # Reset the form
            except Exception as e:
                error_message = "An error occurred while saving your message. Please try again."
        else:
            form_errors = form.errors
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'form_errors': form_errors,
        'success_message': success_message,
        'error_message': error_message,
    })

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def faq(request):
    return render(request, 'faq.html')

def get_free_consultation(request):
    success_message = None
    error_message = None
    form_errors = {}

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = "🚀 Your consultation request has been received. You will receive an email with the meeting details shortly."
                form = ConsultationForm()  # Reset the form
            except Exception as e:
                error_message = "💀 An error occurred while saving your consultation request. Please try again."
        else:
            form_errors = form.errors
    else:
        form = ConsultationForm()

    return render(request, 'get_free_consultation.html', {
        'form': form,
        'form_errors': form_errors,
        'success_message': success_message,
        'error_message': error_message,
    })