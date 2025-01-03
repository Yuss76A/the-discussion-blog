from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    """
    Represents a blog post in the application.

    Attributes:
        title (CharField): The title of the post, limited to 200 characters.
        content (TextField): The main content of the post.
        date_posted (DateTimeField): The date and time when the post was published, 
        automatically set to the current date and time when created.
        author (ForeignKey): A reference to the User model, indicating the author of the post.
        This relationship allows for cascading deletes; if a user is deleted,
        their posts will also be removed.
        Methods:
        __str__(): Returns the title of the post as a string representation.
        get_absolute_url(): Returns the URL to access the detailed view of the post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('blog-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=100)  # Field for the user's name
    email = models.EmailField()                # Field for the user's email
    message = models.TextField()               # Field for the message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the request is created

    def __str__(self):
        return f"Collaboration Request from {self.name}"