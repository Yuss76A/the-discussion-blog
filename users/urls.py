from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# URL patterns for user registration and authentication in the application
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('account/', views.account_views, name='account'),  
    path('login/', auth_views.LoginView.as_view(), name='login'),
]