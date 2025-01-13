from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, AccountUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Account


def register_view(request):
    """
    Handle user registration.

    This view processes the registration form submission. If the request method is POST, 
    it validates the submitted form data and creates a new user account. Upon successful 
    registration, the user is logged in, and a success message is displayed. If the request 
    method is GET, it initializes a blank form for registration.

    Parameters:
        request: The HTTP request object.

    Returns:
        Rendered template for registration or redirects to the login page on success.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = user.username 
            messages.success(request, f'Welcome, {username}! Your account is ready. Log in to continue.')  
            return redirect('login')  
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def account(request):
    """
    Display user account information.

    This view requires the user to be logged in. It renders a template displaying the
    user's account details.

    Parameters:
        request: The HTTP request object.

    Returns:
        Rendered template for the user's account information.
    """
    return render(request, 'users/account.html')


@login_required
def update_account(request):
    """
    Update user account information.

    This view allows logged-in users to update their account details. It handles both
    user-related information and account-related details. Upon successful form submission,
    the user's updated information is saved, and a success message is displayed.

    Parameters:
        request: The HTTP request object.

    Returns:
        Rendered template for the account update form, or redirects to the account page
        on successful update.
    """
    user_account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)  

        if user_form.is_valid() and account_form.is_valid():
            user_form.save() 
            account_form.save()  
            messages.success(request, 'Your account has been successfully updated!')  
            return redirect('account') 
            
    else:
        user_form = UserUpdateForm(instance=request.user)
        account_form = AccountUpdateForm(instance=request.user.account)
    context = {
        'user_form': user_form,
        'account_form': account_form
        }
    return render(request, 'users/account_update.html', context)  