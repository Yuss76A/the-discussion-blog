from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Account(models.Model):
    """
    Represents a user account that holds additional information linked to Django's User model.
    
    Attributes:
    user (OneToOneField): A one-to-one relationship with the User model.
    avatar (ImageField): The profile image for the user, with a default image set.
    """  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    avatar = CloudinaryField('image', default='default_avatar') 

    def __str__(self):
        return f"{self.user.username}'s Account"
        