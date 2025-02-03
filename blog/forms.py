from django import forms
from .models import Comment, CollaborateRequest


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments on posts.

    This form utilizes Django's ModelForm to create a form that allows users to
    input content for their comments. The content is expected to be well-formed
    as defined by the Comment model.

    Attributes:
        content (Textarea): A textarea widget for entering comment content,
                             with placeholder text and specified row height.

    Meta:
        model (Comment): The model this form is associated with.
        fields (list): List containing the fields from the Comment model to
        display.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Add a comment...',
                    'rows': 4
                }
            ),
        }


class CollaborateForm(forms.ModelForm):
    """
    A form for submitting collaboration requests.

    This form allows users to provide their name, email, and message for
    collaboration inquiries. It utilizes Django's ModelForm to facilitate the
    gathering of necessary information to process these requests.

    Attributes:
        name (CharField): The name of the user making the request.
        email (EmailField): The email address of the user.
        message (Textarea): A textarea widget for entering the message,
                            with placeholder text and specified row height.

    Meta:
        model (CollaborateRequest): The model this form is associated with.
        fields (list): List containing the fields from the CollaborateRequest
        model to display.
    """
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message...',
                'rows': 6,
                'class': 'custom-textarea'
            }),
        }
