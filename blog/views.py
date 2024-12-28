from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm


# def welcome(request):
#     context = {
#         'articles': Post.objects.all()
#     }
#     return render(request, 'blog/welcome.html', context)

# About page view
def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


# Post detail view
# def post_detail(request, pk):
#     post = get_object_or_404(Post, id=pk)  # Get the post by primary key
#     comments = post.comments.all()  # Retrieve associated comments

#     # Handle comment submission
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         if request.user.is_authenticated:
#             Comment.objects.create(post=post, author=request.user, content=content)  # Create new comment
#             messages.success(request, 'Your comment has been added!')
#             return redirect('blog-detail', pk=post.id)  # Redirect to the detail view of the post

#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})
    

# List of all posts view
class PostListView(ListView):
    model = Post
    template_name = 'blog/welcome.html'
    context_object_name = 'articles'
    ordering = ["-date_posted"]

# Detail view for a specific post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'  # Name the context object for access in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  # Include comments in context
        context['comment_form'] = CommentForm()  # Initialize the comment form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)  # Create a form instance with submitted data
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Link the comment to the post
            comment.author = request.user  # Set the comment author
            comment.save()  # Save the comment
            messages.success(request, 'Your comment has been added!')
            return redirect('blog-detail', pk=self.object.id)  # Redirect back to post detail

        # If the form is not valid, render the same page with form errors
        context = self.get_context_data()
        context['comment_form'] = form  # Include the invalid form to show errors
        return self.render_to_response(context)
  

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