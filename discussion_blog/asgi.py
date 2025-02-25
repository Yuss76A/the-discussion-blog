import os

from django.core.asgi import get_asgi_application

# Set the default setting module for the Django application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussion_blog.settings')

# Initialize the ASGI application with the given settings
application = get_asgi_application()
