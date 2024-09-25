from django.shortcuts import render, get_object_or_404
from .models import Portfolio
import markdown
from helpers.cache.page_cache import cache_if_not_debug

@cache_if_not_debug(60 * 60 * 15) # Cache for 15 minutes
def portfolios(request):
    category = request.GET.get('category')
    if category:
        portfolios = Portfolio.objects.filter(category=category).only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
    else:
        portfolios = Portfolio.objects.only('id', 'title', 'date', 'short_description', 'thumbnail', 'slug').order_by('-date')
    
    for portfolio in portfolios:
        portfolio.technologies_list = portfolio.technologies.split(',')
    
    return render(request, 'portfolio.html', {'portfolios': portfolios})

@cache_if_not_debug(60 * 60 * 15) # Cache for 15 minutes
def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    portfolio.long_description = markdown.markdown(portfolio.long_description, extensions=['extra'])
    portfolio.technologies_list = portfolio.technologies.split(',')
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})