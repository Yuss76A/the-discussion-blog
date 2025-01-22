from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Account  


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    """
    Create an Account instance for a newly created User.

    This signal is triggered when a User instance is saved and if it's a new instance.
    It creates a corresponding Account instance automatically upon user registration.
    """
    if created:
        Account.objects.create(user=instance)  


@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
    """
    Save the Account instance whenever the User instance is saved.

    This keeps the related Account in sync with the User's data, ensuring that any updates 
    to the User instance are reflected in the corresponding Account instance.
    """
    instance.account.save()  