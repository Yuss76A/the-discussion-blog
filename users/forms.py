from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account


class UserRegisterForm(UserCreationForm):
    """
    Form for user registration, allowing input of username, first name, last name, and email.
    
    Inherits from UserCreationForm for built-in validation and password handling.
    This form requires the username, first name, last name, and email fields.
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating the user's account, specifically for changing the avatar image,
    username, and name (first and last).

    This form allows users to upload a new avatar image for their account as well as
    update their name and username. The avatar will be saved using the Cloudinary field 
    in the Account model. Updating the name and username is optional.
    """
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if username:
            if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
                raise forms.ValidationError("This username is already taken.")
        return username  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise forms.ValidationError("This email is already associated with another account.")
        return email
        

class AccountUpdateForm(forms.ModelForm):
    """
    Form for updating the user's account, specifically for changing the avatar image.
    """
    class Meta:
        model = Account  
        fields = ['avatar'] 