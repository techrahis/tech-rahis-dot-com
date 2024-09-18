from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('search/', views.blog_search, name='blog_search'),
    path('category/<slug:slug>/', views.blog_category, name='blog_category'),
    path('tag/<slug:slug>/', views.blog_tag, name='blog_tag'),
]