from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate
def home(request):
    # return HttpResponse("Hello you are at the home page")
    return render(request, 'website/index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist.")
            return redirect('login_page')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect('login_page')

        login(request, user)
        messages.success(request, "Login successful.")
        return redirect('all_blogs:all_blogs') 

    return render(request, 'website/login.html')

def register_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
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