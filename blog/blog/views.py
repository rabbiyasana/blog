from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    # return HttpResponse("Hello you are at the home page")
    return render(request, 'website/index.html')


def login_page(request):
    # return HttpResponse("Hello you are at the login page")
    return render(request, 'website/login.html')

def register_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register_page')

        User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Account created successfully.")
        return redirect('login_page')



    return render(request, 'website/register.html')