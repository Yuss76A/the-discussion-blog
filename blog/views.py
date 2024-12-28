from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def welcome(request):
#     context = {
#         'articles': Post.objects.all()
#     }
#     return render(request, 'blog/welcome.html', context)

# About page view
def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


# Post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()  
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if request.user.is_authenticated:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, 'Your comment has been added!')
            return redirect('blog-detail', pk=post.id)  

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})  
    

# List of all posts view
class PostListView(ListView):
    model = Post
    template_name = 'blog/welcome.html'
    context_object_name = 'articles'
    ordering = ["-date_posted"]

# Detail view for a specific post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

# Create new post view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created successfully!')
        return super().form_valid(form)

# Update existing post view with permissions check
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete post view with permissions check
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False