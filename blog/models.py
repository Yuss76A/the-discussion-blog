from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    """
    Represents a category for blog posts.

    Attributes:
        name (CharField): The name of the category.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

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
        likes (IntegerField): The number of likes for the post, default is 0.
        dislikes (IntegerField): The number of dislikes for the post, default is 0.

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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')


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
        author (ForeignKey): A reference to the User object representing the author of the comment.
        content (TextField): The textual content of the comment.
        created_at (DateTimeField): The date and time when the comment was created; 
                                     automatically set to now.
        likes (IntegerField): The number of likes for the comment, default is 0.
        dislikes (IntegerField): The number of dislikes for the comment, default is 0.
        parent (ForeignKey, optional): A self-referencing ForeignKey linking to another 
                                       Comment object (for replies).

    Methods:
        __str__(): Returns a string representation of the comment, displaying the author's 
                    username and a truncated version of the content.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collaboration Request from {self.name}"


class Notification(models.Model):
    """
    Represents a notification for a user within the application.

    Notifications can relate to various events, such as comments on the user's posts
    or replies to their comments. Each notification is associated with a specific user,
    and may include additional information based on the type of notification.

    Attributes:
        user (User): The user associated with this notification.
        message (str): A message describing the notification.
        comment (Comment, optional): A reference to a Comment object that this notification pertains to.
        created_at (datetime): The timestamp when the notification was created.
        is_read (bool): A flag indicating whether the notification has been read by the user.

    Methods:
        __str__(): Returns a string representation of the notification.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.username}: {self.message}'
