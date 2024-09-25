from django.views.decorators.cache import cache_page
from django.conf import settings

def cache_if_not_debug(timeout):
    """Decorator to cache a view only if DEBUG is False."""
    def decorator(view_func):
        if settings.DEBUG:
            return view_func

        return cache_page(timeout)(view_func)
    return decorator