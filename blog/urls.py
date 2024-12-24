from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('about/', views.about, name="about"),
    path('post/<int:id>/', views.post_detail, name='blog-detail'),
]