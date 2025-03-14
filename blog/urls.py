"""
URL routing for the blog application.

This module defines the URL patterns for navigating various views in the
blog application, including post management, comments, notifications,
and user interactions.
"""

from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    update_comment,
    delete_comment,
    support_and_collaboration,
    like_post,
    dislike_post,
    like_comment,
    dislike_comment,
    notifications_view,
    reply_comment,
    delete_notification
)


# URL patterns for blog application navigation
urlpatterns = [
    path('', PostListView.as_view(), name="welcome"),
    path('about/', views.about, name="about"),
    path('highlights/', views.highlights, name="highlights"),
    path('support-and-collaboration/',
         support_and_collaboration,
         name='support-and-collaboration'
         ),
    path('about-me/', views.about_me, name='about-me'),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update/',
         PostUpdateView.as_view(),
         name='blog-update'
         ),
    path('post/<int:pk>/delete/',
         PostDeleteView.as_view(),
         name="blog-delete"
         ),
    path('comment/<int:comment_id>/update/',
         update_comment,
         name='update-comment'
         ),
    path('comment/<int:comment_id>/delete/',
         delete_comment,
         name='delete-comment'
         ),
    path('post/<int:post_id>/like/', like_post, name='like-post'),
    path('post/<int:post_id>/dislike/', dislike_post, name='dislike-post'),
    path('comment/<int:comment_id>/like/', like_comment, name='like-comment'),
    path('comment/<int:comment_id>/dislike/',
         dislike_comment,
         name='dislike-comment'
         ),
    path('notifications/', notifications_view, name='notifications'),
    path('comment/<int:comment_id>/reply/',
         reply_comment,
         name='reply-comment'
         ),
    path('notifications/delete/<int:notification_id>/',
         delete_notification,
         name='delete_notification'
         ),
]
