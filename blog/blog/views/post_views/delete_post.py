from django.shortcuts import get_object_or_404, redirect
from all_blogs.models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def delete_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully.")
        return redirect('all_blogs') 

    return redirect('all_blogs')