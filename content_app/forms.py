from dataclasses import fields
from django.forms import ModelForm
from content_app.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class EditBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']