from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def one_page(request):
    return render(request, 'onepage.html')
