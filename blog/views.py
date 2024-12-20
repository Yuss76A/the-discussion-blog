from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

posts = [
    {
    'id': 1,
    'author': 'DK76Yuss',
    'title': 'Blog Post 1',
    'content': 'This is my first blog post',
    'date_posted': '18th December, 2024',
    },
    {
    'id': 2,
    'author': 'MettPro26',
    'title': 'Blog Post 2',
    'content': 'This is my second blog post',
    'date_posted': '20th December, 2024',
    }
]

def welcome(request):
    context = {
        'articles': posts
    }
    return render(request, 'blog/welcome.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('blog-welcome')  
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def post_detail(request, id):
    post = get_object_or_404(posts, id=id)  
    return render(request, 'blog/post_detail.html', {'post': post})  