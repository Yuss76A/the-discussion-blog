"""
Admin configuration for the Users application.

This module registers the Account model with the Django admin interface, allowing 
for management of user accounts through the admin portal.
"""


from django.contrib import admin
from .models import Account 


admin.site.register(Account)