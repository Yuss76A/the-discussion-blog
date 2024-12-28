from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the Blog application in the Django project.
    
    This class sets the default primary key field type to BigAutoField,
    which is appropriate for large data sets to prevent integer overflow.
    It also specifies the name of the application as 'blog', which Django uses
    to reference this app throughout the project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
