from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = user.username 
            messages.success(request, f'Welcome, {username}! Your account is ready. Log in to continue.')  
            return redirect('welcome')  
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
