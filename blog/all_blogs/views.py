from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs= Blog.objects.all()
    return render(request, 'all_blogs/all_blogs.html', {'blogs': blogs})