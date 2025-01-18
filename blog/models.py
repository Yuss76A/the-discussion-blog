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
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

def __str__(self):
    """Return the title of the post as its string representation."""
    return self.title

def get_absolute_url(self):
    """Return the URL for the detail view of the post based on its primary key."""
    return reverse('blog-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): A reference to the associated Post object.
                           This creates a one-to-many relationship where a post can have multiple comments.
        author (ForeignKey): A reference to the User object representing the author of the comment.
        content (TextField): The textual content of the comment.
        created_at (DateTimeField): The date and time when the comment was created; automatically set to now.

    Methods:
        __str__(): Returns a string representation of the comment, displaying the author's username and a truncated version of the content.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"


class CollaborateRequest(models.Model):
    """
    Represents a collaboration request submitted by a user.

    Attributes:
        name (CharField): The name of the user submitting the request.
        email (EmailField): The email address of the user for follow-up.
        message (TextField): The content of the message detailing the collaboration inquiry.
        created_at (DateTimeField): The date and time when the request was created; automatically set to now.

    Methods:
        __str__(): Returns a string representation of the collaboration request showing the user's name.
    """
    name = models.CharField(max_length=100)  # Field for the user's name
    email = models.EmailField()                # Field for the user's email
    message = models.TextField()               # Field for the message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the request is created

    def __str__(self):
        return f"Collaboration Request from {self.name}"