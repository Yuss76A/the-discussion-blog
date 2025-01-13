import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussion_blog.settings')

# Instantiate the WSGI application for the Django project
application = get_wsgi_application()
