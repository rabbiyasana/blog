from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')
def all_blogs(request):
    blogs= Blog.objects.all()
    return render(request, 'all_blogs/all_blogs.html', {'blogs': blogs})

@login_required(login_url='login_page')
def blog_details(request,blog_id):
    blog= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'all_blogs/blog_details.html', {'blog': blog})