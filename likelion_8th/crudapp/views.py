from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import PostForm

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')


def postupdate(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', blog_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    post.delete()
    return redirect('home')