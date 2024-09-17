from django.shortcuts import render, get_object_or_404
from .models import Portfolio
import markdown

def portfolios(request):
    category = request.GET.get('category')
    if category:
        portfolios = Portfolio.objects.filter(category=category).only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
    else:
        portfolios = Portfolio.objects.only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
    
    for portfolio in portfolios:
        portfolio.technologies_list = portfolio.technologies.split(',')
    
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    portfolio.long_description = markdown.markdown(portfolio.long_description, extensions=['extra'])
    portfolio.technologies_list = portfolio.technologies.split(',')
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})



# from django.shortcuts import render, get_object_or_404
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# from .models import Project
# import markdown

# @cache_page(60 * 15)  # Cache for 15 minutes
# def projects(request):
#     # Check cache first
#     cache_key = 'projects_list'
#     cached_projects = cache.get(cache_key)

#     if cached_projects is not None:
#         projects = cached_projects
#     else:
#         projects = Project.objects.all()
#         for project in projects:
#             project.long_description = markdown.markdown(project.long_description, extensions=['extra'])
#         # Cache the projects
#         cache.set(cache_key, projects, timeout=60 * 15)

#     return render(request, 'projects.html', {'projects': projects})

# @cache_page(60 * 15)  # Cache for 15 minutes
# def project_detail(request, project_id):
#     # Check cache first
#     cache_key = f'project_detail_{project_id}'
#     cached_project = cache.get(cache_key)

#     if cached_project is not None:
#         project = cached_project
#     else:
#         project = get_object_or_404(Project, id=project_id)
#         project.long_description = markdown.markdown(project.long_description, extensions=['extra'])
#         # Cache the project detail
#         cache.set(cache_key, project, timeout=60 * 15)

#     return render(request, 'project_detail.html', {'project': project})
