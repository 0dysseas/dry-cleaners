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
    contact_form = ContactForm()
    return render(request, 'contact.html', {'form': contact_form})


def one_page(request):
    return render(request, 'onepage.html')
