from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CalculationForm, ContactForm


def index(request):

    if request.method == 'GET':
        calculation_form = CalculationForm()
    else:
        calculation_form = CalculationForm(request.POST)

        if calculation_form.is_valid():
            carpet_types = calculation_form.cleaned_data['carpet_types']
            meters = calculation_form.cleaned_data['meters']

            return HttpResponseRedirect(reverse('cleaners:services'))

    return render(request, 'index.html', {'form': calculation_form})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pick_up(request):
    return render(request, 'city-guides.html')


def thank_you(request):
    return render(request, 'thank-you.html')


# Using function-based view instead of the generic class based FormView in order to have
# better control of the form processing
def contact(request):

    # If this is a GET request create the contact form
    if request.method == 'GET':
        contact_form = ContactForm()
    # If this is a POST request then process the data
    else:
        # Create a form instance and bind the data request to it
        contact_form = ContactForm(request.POST)

        # Check if the form is valid and process its data
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            email_from = contact_form.cleaned_data['email_from']
            message = contact_form.cleaned_data['message']

            try:
                send_mail(subject, message, email_from, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(reverse('cleaners:thank_you'))

    return render(request, 'contact.html', {'form': contact_form})


def one_page(request):
    return render(request, 'onepage.html')
