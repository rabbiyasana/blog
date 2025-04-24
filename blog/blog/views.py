from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello you are at the home page")
    return render(request, 'website/index.html')