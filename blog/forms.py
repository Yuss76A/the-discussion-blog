from django import forms
from .models import Comment, CollaborateRequest

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add a comment...', 'rows': 4}),
        }


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
        widgets = {  
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message...', 
                'rows': 6,  # Increase rows for bigger message area
                'class': 'custom-textarea'  # Add a custom class for CSS styling
            }),
        }