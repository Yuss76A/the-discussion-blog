from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    # path('', views.welcome, name="welcome"),

    path('', PostListView.as_view(), name="welcome"),
    path('about/', views.about, name="about"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    # path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='blog-update'),    
]