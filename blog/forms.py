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
        widgets = {  # Optional: Customize form widgets for better UX
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 4}),
        }