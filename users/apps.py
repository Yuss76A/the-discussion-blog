from django.apps import AppConfig



class UsersConfig(AppConfig):
    """
    Configuration class for the Users application.

    This class contains configuration settings for the Users app within the Django project.
    It specifies the default auto field type to be used for models and sets the name of the 
    application to be 'users'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        This method runs when the application is ready.

        It is used to import signal handlers defined in the 'signals.py' file, ensuring
        that the related signal actions are set up when the application starts.
        """
        import users.signals
