from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CalculationForm, ContactForm


def index(request):

    if request.method == 'GET':
        calculation_form = CalculationForm()
    # else:
    #     calculation_form = CalculationForm(request.POST)  # TODO-me: Is this POST handling needed?
    #
    #     if calculation_form.is_valid():
    #         carpet_types = calculation_form.cleaned_data['carpet_types']
    #         length = calculation_form.cleaned_data['length']
    #         width = calculation_form.cleaned_data['width']
    #
    #         return HttpResponseRedirect(reverse('cleaners:services'))

    return render(request, 'index.html', {'form': calculation_form})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pick_up(request):
    # If this is a GET request create the calculation form
    if request.method == 'GET':
        calculation_form_pickup = CalculationForm()
    else:
        calculation_form_pickup = CalculationForm(request.POST)

        if calculation_form_pickup.is_valid():
            carpet_type = calculation_form_pickup.cleaned_data['carpet_types']
            length = calculation_form_pickup.cleaned_data['length']
            width = calculation_form_pickup.cleaned_data['width']
            service_cost = request.POST.get('service_cost')

            return render(request, 'pickup_delivery.html', {'service_cost': service_cost, 'carpet_type': carpet_type,
                                                            'length': length, 'width': width})

    return render(request, 'pickup_delivery.html', {'form': calculation_form_pickup})


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
