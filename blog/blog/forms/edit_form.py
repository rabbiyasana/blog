from django import forms
from all_blogs.models import Blog

class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'price', 'image']