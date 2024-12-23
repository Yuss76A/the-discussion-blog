from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('account/', views.account_view, name='account'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]