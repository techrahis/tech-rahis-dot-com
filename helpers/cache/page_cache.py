import logging
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from core.models import SiteData
import time

logger = logging.getLogger(__name__)

def cache_if_not_debug(timeout, revalidate_key):
    """Decorator to cache a view only if DEBUG is False and revalidate based on a timestamp."""
    def decorator(view_func):
        if settings.DEBUG:
            return view_func

        def wrapped_view(request, *args, **kwargs):
            try:
                cache_key = f'{revalidate_key}_timestamp'
                last_revalidate = cache.get(cache_key)
                revalidate = SiteData.objects.only('revalidate').first()

                if not revalidate:
                    logger.warning("No SiteData instance found.")
                elif not last_revalidate or revalidate.revalidate != last_revalidate:
                    logger.info("Revalidating cache.")
                    cache.clear()  # Clear the cache if the timestamp has changed or is not found
                    cache.set(cache_key, revalidate.revalidate if revalidate else time.time(), timeout)

                return cache_page(timeout)(view_func)(request, *args, **kwargs)
            except Exception as e:
                logger.error(f"Error in cache_if_not_debug: {e}")
                raise

        return wrapped_view
    return decorator