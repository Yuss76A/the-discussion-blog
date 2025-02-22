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

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name='reset_password'),
    
    path('reset_password_done/',
        auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
        name='password_reset_confirm'),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
        name='password_reset_complete'),
]
