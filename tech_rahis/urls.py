from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("blogs/", include("blogs.urls")),
    path("portfolios/", include("portfolios.urls")),
]