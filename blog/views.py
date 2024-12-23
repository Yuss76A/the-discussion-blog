from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Post


def welcome(request):
    context = {
        'articles': Post.objects.all()
    }
    return render(request, 'blog/welcome.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  
    return render(request, 'blog/post_detail.html', {'post': post})  