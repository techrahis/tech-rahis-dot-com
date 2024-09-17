from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolios, name='portfolios'),
    path('<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
]