from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Represents a user account that holds additional information linked to Django's User model.
    
    Attributes:
    user (OneToOneField): A one-to-one relationship with the User model.
    avatar (ImageField): The profile image for the user, with a default image set.
    """  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    avatar = models.ImageField(default='default.jpg', upload_to='images/')  

    def __str__(self):
        return f"{self.user.username}'s Account"
        