from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogCategory, Tag
import markdown

def blog_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    
    blogs = Blog.objects.all()

    # Filter by query (search)
    if query:
        blogs = blogs.filter(title__icontains=query).only('id', 'title', 'short_description', 'thumbnail', 'slug').order_by('-date')

    # Filter by category
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        blogs = blogs.filter(category=category).only('id', 'title', 'short_description', 'thumbnail', 'slug').order_by('-date')

    # Filter by tag
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags=tag).only('id', 'title', 'short_description', 'thumbnail', 'slug').order_by('-date')
    
    # Pagination
    paginator = Paginator(blogs, 5)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Fetch all categories and tags for dynamic rendering
    categories = BlogCategory.objects.all()
    tags = Tag.objects.all()

    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'tags': tags,
        'category': category if category_slug else None,
        'tag': tag if tag_slug else None,
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, slug):
    # Get the blog by slug or return a 404 if not found
    blog = get_object_or_404(Blog, slug=slug)
    blog.long_description = markdown.markdown(blog.long_description, extensions=['extra'])
    # Pass the blog object to the template
    context = {
        'blog': blog,
    }
    return render(request, 'blog_detail.html', context)