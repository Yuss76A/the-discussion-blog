from django.contrib import admin
from django.urls import path, include
from blog import views as index_views
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

# URL configuration for the Django project, mapping URL paths to their respective views for
# the blog and user accounts functionalities, including admin access, authentication, and 
# media file handling in development mode.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register_view, name='register'),
    path('account/', user_views.account, name='account'),
     path('account/update/', user_views.update_account, name='update_account'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout")
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
