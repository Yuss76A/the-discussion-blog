from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account


class UserRegisterForm(UserCreationForm):
    """
    Form for user registration, allowing input of username, first name, last name, and email.
    Inherits from UserCreationForm for built-in validation and password handling.
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user information, specifically for editing username and email.
    Includes custom validation to ensure the email is unique among users.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already associated with another account.")
        return email
        

class AccountUpdateForm(forms.ModelForm):
    """
    Form for updating the user's account, specifically for changing the avatar image.
    """
    class Meta:
        model = Account  
        fields = ['avatar'] 