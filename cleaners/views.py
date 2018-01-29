from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    # return HttpResponse('Dry Cleaners')
    return render(request, 'index.html')


def one_page(request):
    # return HttpResponse('Dry Cleaners')
    return render(request, 'onepage.html')
