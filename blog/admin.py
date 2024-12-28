from django.contrib import admin
from .models import Post

# Register the Post model with the Django admin site.
# This allows admins to create, read, update, and delete posts from the admin interface.
admin.site.register(Post)
