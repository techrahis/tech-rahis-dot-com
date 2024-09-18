from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogCategory, Tag

def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})

def blog_search(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(title__icontains=query) if query else Blog.objects.all()
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj, 'query': query})

def blog_category(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)
    blogs = Blog.objects.filter(category=category)
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj, 'category': category})

def blog_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Blog.objects.filter(tags=tag)
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj, 'tag': tag})