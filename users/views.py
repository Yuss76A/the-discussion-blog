from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, AccountUpdateForm 

def register_view(request):
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
    return render(request, 'users/account.html')


@login_required
def update_account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.useraccount)  

        if user_form.is_valid() and account_form.is_valid():
            user_form.save() 
            account_form.save()  
            messages.success(request, 'Your account has been successfully updated!')  
            return redirect('account') 

    else:
        
        user_form = UserUpdateForm(instance=request.user)
        account_form = AccountUpdateForm(instance=request.user.useraccount)

    context = {
        'user_form': user_form,
        'account_form': account_form
    }
    return render(request, 'users/edit_account.html', context)  
