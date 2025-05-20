from django.shortcuts import render, get_object_or_404, redirect
from all_blogs.models import Blog
from blog.forms.edit_form import EditForm  

def edit_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_details', blog_id=blog_id)  # or wherever your blog detail page is
    else:
        form = EditForm(instance=blog)
    
    return render(request, 'blog_details.html', {'form': form, 'blog': blog, 'blog_id': blog_id})