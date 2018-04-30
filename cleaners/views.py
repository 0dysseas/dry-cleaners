from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def pick_up(request):
    return render(request, 'city-guides.html')


def contact(request):
    return render(request, 'contact.html')  # TODO-me: Utilize django's contact form


def one_page(request):
    return render(request, 'onepage.html')
