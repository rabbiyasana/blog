from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello you are at the home page")
    return render(request, 'website/index.html')


def login_page(request):
    # return HttpResponse("Hello you are at the login page")
    return render(request, 'website/login.html')

def register_page(request):
    # return HttpResponse("Hello you are at the login page")
    return render(request, 'website/register.html')