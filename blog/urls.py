from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, update_comment, delete_comment, support_and_collaboration


# URL patterns for blog application navigation
urlpatterns = [
    path('', PostListView.as_view(), name="welcome"),
    path('about/', views.about, name="about"),
    path('highlights/', views.highlights, name="highlights"),
    path('support-and-collaboration/', views.support_and_collaboration, name='support-and-collaboration'),
    path('about-me/', views.about_me, name='about-me'),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    path('comment/<int:comment_id>/update/', update_comment, name='update-comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
]