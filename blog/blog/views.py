import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail
from django.conf import settings
from all_blogs.models import UserProfile


def home(request):
    # return HttpResponse("Hello you are at the home page")
    return render(request, 'website/index.html')

def generate_otp():
    return str(random.randint(1000, 9999))


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('login_page')

        if not user.userprofile.is_email_verified:
            messages.error(request, "Please verify your email before logging in.")
            return redirect('login_page')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect('login_page')

        login(request, user)
        messages.success(request, "Login successful.")
        return redirect('all_blogs') 

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
 
        user=User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password
        )

        otp = generate_otp()
        user.userprofile.email_otp = otp
        user.userprofile.save()

        send_mail(
    'Your OTP Code',
    f'Your OTP is: {otp}',
    settings.EMAIL_HOST_USER,
    [user.email],
    fail_silently=False,
)
        messages.success(request, "Account created. Please verify your email.")
        return redirect('verify_email', user_id=user.id)  

    return render(request, 'website/register.html')

def verify_email(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        profile = user.userprofile
        if entered_otp == profile.email_otp:
            profile.is_email_verified = True
            profile.email_otp = None
            profile.save()
            messages.success(request, "Email verified! You can login now.")
            return redirect('login_page')
        else:
            messages.error(request, "Incorrect OTP.")

    return render(request, 'website/verify_email.html', {'user': user})


def logout_page(request):   
    
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')  
