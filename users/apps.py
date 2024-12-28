from django.apps import AppConfig


# Configuration for the Users application in the Django project
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        This method runs when the application is ready.
        Used to import signal handlers defined in the 'signals.py' file.
        """
        import users.signals
