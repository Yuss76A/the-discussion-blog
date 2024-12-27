from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages


# def welcome(request):
#     context = {
#         'articles': Post.objects.all()
#     }
#     return render(request, 'blog/welcome.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  
    return render(request, 'blog/post_detail.html', {'post': post})

class PostListView(ListView):
    model = Post
    template_name = 'blog/welcome.html'
    context_object_name = 'articles'
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created successfully!')
        return super().form_valid(form)