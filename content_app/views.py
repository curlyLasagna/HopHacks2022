from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import block
from requests import request
from content_app.forms import BlogForm, EditBlogForm
from content_app.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    blogs = Blog.objects.all()

    return render(request, 'home.html', {'blogs': blogs})

@login_required
def add_blog(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'add-blog.html', {'form': form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            Blog.objects.create(title=title, content=content, user_id=request.user.id)
            
            return redirect('home')
        else:
            return render(request, 'add-blog.html', {'form': form})

@login_required(login_url='login')
def delete_blog(request, id):
    #Blog.objects.get(id=id).delete()
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        messages.error(request, 'Deletion failed')
        messages.error(request, 'Blog does not exist')
        return redirect('404')
    blog.delete()

    return redirect('home')

@login_required
def edit_blog(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        messages.error(request, 'Blog does not exist')
        return redirect('404')
    
    if request.method == 'GET':
        form = EditBlogForm(instance=blog)
        return render(request, 'edit-blog.html', {'form': form})   

    else:
        form = EditBlogForm(request.POST) 
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']

            blog.save()
            return redirect('home')

def not_found(request):
    return render(request, 'core/404.html')
