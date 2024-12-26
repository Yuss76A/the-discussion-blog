from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView


urlpatterns = [
    # path('', views.welcome, name="welcome"),
    path('about/', views.about, name="about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('', PostListView.as_view(), name="blog-welcome")
    
]