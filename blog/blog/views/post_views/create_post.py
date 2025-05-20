from django.shortcuts import render, redirect
from django.contrib import messages
from all_blogs.models import Blog

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        body = request.POST.get('body', '').strip()
        blog_type = request.POST.get('blog_type', '').strip()
        price = request.POST.get('price', '0').strip()
        image = request.FILES.get('image')

        if not title or not body:
            messages.error(request, "Title and content are required.")
            return redirect('create_post')

        try:
            price = float(price)
        except ValueError:
            messages.error(request, "Invalid price.")
            return redirect('create_post')
        
        blog= Blog.objects.create(
            user=request.user,
            title=title,
            body=body,
            image=image,
            blog_type=blog_type,
            price=price
        )
        messages.success(request, "Post created successfully.")
        return redirect('all_blogs')  # Redirect to the all blogs page

    return render(request, 'website/post/create_post.html')