from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pick_up(request):
    return render(request, 'city-guides.html')


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
            name = contact_form.cleaned_data['name']
            email_from = contact_form.cleaned_data['email_from']
            message = contact_form.cleaned_data['message']

    return render(request, 'contact.html', {'form': contact_form})


def one_page(request):
    return render(request, 'onepage.html')
