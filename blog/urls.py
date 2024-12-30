from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, update_comment, delete_comment


# URL patterns for blog application navigation
urlpatterns = [
    # path('', views.welcome, name="welcome"),

    path('', PostListView.as_view(), name="welcome"),
    path('about/', views.about, name="about"),
    path('highlights/', views.highlights, name="highlights"),
    path('about-me/', views.about_me, name='about-me'),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    # path('post/<int:pk>/', post_detail, name="blog-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    path('comment/<int:comment_id>/update/', update_comment, name='update-comment'),  # Update comment URL
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
]