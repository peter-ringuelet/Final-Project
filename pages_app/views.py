from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from .forms import BlogForm

from django.contrib.auth.decorators import login_required


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/home.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

@login_required
def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog-detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_update.html', {'form': form})

@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog-detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog-page')
