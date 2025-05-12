import random

from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.core.mail import send_mail
from django.conf import settings
from all_blogs.models import UserProfile


def home(request):
    
    return render(request, 'website/index.html')

def generate_otp():
    return str(random.randint(1000, 9999))


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is None:
            messages.error(request, "Invalid credentials or user does not exist.")
            return redirect('login_page')
        
        print(f"Uverification status: {user.userprofile.is_email_verified}")
        # Check if email is verified
        if not user.userprofile.is_email_verified:
            messages.error(request, "Please verify your email before logging in.")
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

        otp = generate_otp()

        request.session['pending_registration'] = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'email': email,
            'password': password,
            'otp': otp,
        }

        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        messages.success(request, "OTP sent to your email. Please verify.")
        return redirect('verify_email') 

    return render(request, 'website/register.html')


def verify_email(request):
    data = request.session.get('pending_registration')

    if not data:
        messages.error(request, "Session expired or invalid access.")
        return redirect('register_page')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        if entered_otp == data.get('otp'):
            user = User.objects.create_user(
                first_name=data['firstname'],
                last_name=data['lastname'],
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            print(f"User created: {user}")
            # Set email verification flag to True
            user.userprofile.is_email_verified = True
            print(f"Uverification status: {user.userprofile.is_email_verified}")
            user.userprofile.save()

            # Clear session after account creation
            del request.session['pending_registration']

            messages.success(request, "Email verified! You can now log in.")
            return redirect('login_page')
        else:
            messages.error(request, "Invalid OTP. Try again.")

    return render(request, 'website/verify_email.html')


def logout_page(request):   
    
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')  
