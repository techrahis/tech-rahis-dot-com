from django.shortcuts import render
from .forms import *
from portfolios.models import Portfolio

def home(request):
    portfolios = Portfolio.objects.only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
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
    return render(request, 'get_free_consultation.html')