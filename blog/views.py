from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'DK76Yuss',
    'title': 'Blog Post 1',
    'content': 'This is my first blog post',
    'date_posted': '18th December, 2024',
    },
    {
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
