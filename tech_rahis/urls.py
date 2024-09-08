from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("blogs/", include("blogs.urls")),
    path("projects/", include("projects.urls")),
]