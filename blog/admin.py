from django.contrib import admin
from .models import Post, Comment, CollaborateRequest, Category


class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the CollaborateRequest model.

    This admin class customizes the display of the CollaborateRequest entries
    in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the list view.
        search_fields (tuple): The fields that can be searched in the list
        view.

    This allows filtering and searching by the requestor's name and email.
    """
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')


# Register the Post model with the Django admin site.
# This allows admins to create, read, update, and delete posts from the admin
# interface.
# Register models in the admin
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CollaborateRequest, CollaborateRequestAdmin)
admin.site.register(Category)
