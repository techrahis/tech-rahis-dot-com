from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

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

def others(request):
    return render(request, 'others.html')


def hire_me(request):
    success_message = None
    error_message = None
    form_errors = {}

    if request.method == 'POST':
        # Include request.FILES to handle file uploads
        form = HireRequestForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                success_message = "Your request has been submitted successfully!"
                form = HireRequestForm()  # Reset the form
            except Exception as e:
                error_message = "An error occurred while submitting your request. Please try again."
        else:
            form_errors = form.errors
    else:
        form = HireRequestForm()

    return render(request, 'hire_me.html', {
        'form': form,
        'form_errors': form_errors,
        'success_message': success_message,
        'error_message': error_message,
    })