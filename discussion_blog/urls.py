from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

# from django.conf import settings
# from django.conf.urls.static import static

# URL configuration for the Django project, mapping URL paths to their
# respective views for
# the blog and user accounts functionalities, including admin access,
# authentication, and media file handling in development mode.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register_view, name='register'),
    path('account/', user_views.account, name='account'),
    path('account/update/', user_views.update_account, name='update_account'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html'
        ),
        name="login"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='users/logout.html'
        ),
        name="logout"
    ),

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html"
        ),
        name='password_reset'
    ),

    path(
        'reset_password_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name='password_reset_complete'
    ),
]

# Serve media files in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)
