from django.contrib import admin
from .models import Account 

# Register the Account model with the Django admin interface to manage user accounts through the admin portal
admin.site.register(Account)