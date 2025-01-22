from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


"""
URL patterns for user registration and authentication in the application.

This module defines the URL patterns for handling user-related views, including
registration, account management, and login. Each pattern maps a URL to a view
function in the views module.
"""


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('account/', views.account, name='account'),  
    path('login/', auth_views.LoginView.as_view(), name='login'),
]