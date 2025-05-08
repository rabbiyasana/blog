from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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

        new_user  = User.objects.create(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
           
        )
        new_user.set_password(password)
        new_user.save()
        return redirect('login_page')


    return render(request, 'website/register.html')