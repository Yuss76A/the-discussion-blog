from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Post, Comment, Notification
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, CollaborateForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# About Page
def about(request):
    """
    Render the About page.

    This view displays information about the application and its purpose.

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Renders the 'about.html' template with the title context.
    """
    return render(request, 'blog/about.html', {'title': "About Page"})


# List of all posts view
class PostListView(ListView):
    """
    A view to display a list of all blog posts in reverse chronological order.

    This view fetches and displays all posts ordered by the date they were posted, 
    with additional support for search functionality. It also includes trending posts
    in the context for additional user engagement.

    Attributes:
        model (Post): The Django model to be used for this view, representing the blog posts.
        template_name (str): The template filename that will render the output of this view (e.g., 'blog/welcome.html').
        context_object_name (str): The name of the context variable that will contain the list of blog articles.
        ordering (list): A list defining the order in which to return articles, with the most recent posts first.
        paginate_by (int): Number of articles displayed per page for pagination.

    Methods:
        get_queryset(): 
            Returns a queryset of blog posts, optionally filtered by a search query found in the URL.

        get_context_data(**kwargs):
            Extends the default context data by adding a list of trending posts
            to provide additional context and user engagement opportunities.

    Usage:
        The view can be accessed through a URL configuration and will automatically
        handle pagination and search queries based on user input from the request.
    """
    model = Post
    template_name = 'blog/welcome.html'
    context_object_name = 'articles'
    ordering = ["-date_posted"]
    paginate_by = 8

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date_posted')
        search_query = self.request.GET.get('search', '')  # Get search query from URL parameters
        
        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(content__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add trending posts to the context.

        This method extends the default context data with trending posts.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: The updated context data including trending posts.
        """
        context = super().get_context_data(**kwargs)
        context['trending_posts'] = Post.objects.order_by('?')[:5]  # Fetch trending posts


        # Add unread_notification count here
        context['unread_count'] = Notification.objects.filter(user=self.request.user, is_read=False).count()
        
        return context


# Detail view for a specific post
class PostDetailView(LoginRequiredMixin, DetailView):
    """
    View to display the details of a specific blog post.

    This view requires user authentication and allows users to view the post
    details, comments associated with this post, and submit new comments.

    Attributes:
        model (Post): The model to be used for this view.
        template_name (str): The template that will be rendered for this view.
        context_object_name (str): The name used to reference the specific post in the template.

    Methods:
        get_context_data(**kwargs): Adds comments and trending posts to the context.
        post(request, *args, **kwargs): Handles form submissions for new comments.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'  

    def get_context_data(self, **kwargs):
        """
        Add comments and trending posts to the context.

        This method extends the default context data with comments and a small list of
        trending posts.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: The updated context data, including comments and trending posts.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['trending_posts'] = Post.objects.order_by('?')[:5] # Include trending posts
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle form submissions for new comments.

        Validates and saves a new comment related to the post.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable-length argument list.
            **kwargs: Keyworded, variable-length argument list.

        Returns:
            HttpResponse: Redirects to the post detail page if successful or renders
            the same page with form errors.
        """
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('blog-detail', pk=self.object.id)

        # If the form is not valid, render the same page with form errors
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
  

# Create new post view
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new post. 

    This view is accessible only to authenticated users. Upon successful form submission, 
    it assigns the current user as the author of the post and displays a success message.

    Attributes:
        model: The database model to use (Post).
        fields: The fields to be included in the form ('title' and 'content').
        success_url: The URL to redirect to after successful creation.
    
    Methods:
        form_valid(form): Assigns the request user as the author of the post and 
                          calls the parent's form_valid method.
    """
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created successfully!')
        return super().form_valid(form)


# Update existing post view with permissions check
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    """
    View to update an existing post. 

    This view requires the user to be logged in and ensures that only the author of the 
    post can make changes. On successful form submission, it updates the post and retains 
    the author as the current user.

    Attributes:
        model: The database model to use (Post).
        fields: The fields to be included in the form ('title' and 'content').
        success_url: The URL to redirect to after successful update.
    
    Methods:
        form_valid(form): Assigns the request user as the author of the post 
                          and calls the parent's form_valid method.
        test_func(): Checks if the current user is the author of the post, 
                     returning True if so, otherwise False.
    """
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
    """
    View to delete a post.

    This view deletes the specified post and requires that the user is the 
    author of the post in order to proceed, ensuring permissions are respected.

    Attributes:
        model: The database model to use (Post).
        success_url: The URL to redirect to after successful deletion. 

    Methods:
        test_func(): Checks if the current user is the author of the post, 
                     returning True if so, otherwise False.
    """
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Update a comment by the author; only authorized users can edit.
def update_comment(request, comment_id):
    """
    Update a specific comment.

    Ensures that the logged-in user is the author of the comment before allowing edits. 
    If the user is authorized and submits valid content, the comment is updated, 
    and a success message is displayed.

    Parameters:
        request: The HTTP request object.
        comment_id: The ID of the comment to be updated.
    
    Returns:
        Redirects to the blog detail page after updating or renders the update 
        comment form if the request method is not POST.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure that the logged-in user is the author of the comment
    if request.user != comment.author:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('blog-detail', pk=comment.post.id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment.content = content  
            comment.save()  
            messages.success(request, 'Your comment has been updated!')
            return redirect('blog-detail', pk=comment.post.id)

    return render(request, 'blog/update_comment.html', {'comment': comment})


# Delete a comment by the author; only authorized users can delete.
def delete_comment(request, comment_id):
    """
    Delete a specific comment.

    This function checks if the logged-in user is the author of the comment before allowing 
    deletion. If authorized, the comment is deleted, and a success message is displayed. 
    Otherwise, an error message is shown.

    Parameters:
        request: The HTTP request object.
        comment_id: The ID of the comment to be deleted.
    
    Returns:
        Redirects to the blog detail page after deletion or shows an error message 
        if permission is denied.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:  
        post_id = comment.post.id  
        comment.delete()  
        messages.success(request, 'Your comment has been deleted!')
        return redirect('blog-detail', pk=post_id)  
    else:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('blog-detail', pk=comment.post.id)


# Highlights Page
def highlights(request):
    """
    Render the highlights page.

    Parameters:
        request: The HTTP request object.
    
    Returns:
        Renders the highlights page template.
    """

    return render(request, 'blog/highlights.html')


# About Me Page
def about_me(request):
    """
    Render the about me page.

    Parameters:
        request: The HTTP request object.
    
    Returns:
        Renders the about me page template.
    """
    return render(request, 'blog/about_me.html')


# Collaboration and Support Page
def support_and_collaboration(request):
    """
    Render the collaboration and support page.

    Displays a form for collaboration requests and handles form submissions.
    If the form is valid, the request is saved and a success message is displayed.

    Parameters:
        request: The HTTP request object.
    
    Returns:
        Redirects to the support and collaboration page on successful form submission 
        or re-renders the page with the form if there are validation errors.
    """
    collaborate_form = CollaborateForm()  

    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():  
            collaborate_form.save()  
            messages.success(request, 'Your request has been submitted successfully!')
            return redirect('support-and-collaboration') 

    return render(request, 'blog/support_and_collaboration.html', {'collaborate_form': collaborate_form})


# Like a post
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Get the post object
    post.likes += 1  # Increment the likes
    post.save()  # Save the post with the updated like count
    messages.success(request, 'You liked this post!')  # Optional success message
    return redirect('blog-detail', pk=post_id)  # Redirect back to the post detail view


# Dislike a post
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Get the post object 
    post.dislikes += 1  # Increment the dislikes
    post.save()  # Save the post with the updated dislike count
    messages.success(request, 'You disliked this post!')  # Optional success message
    return redirect('blog-detail', pk=post_id)  # Redirect back to the post detail view


# Like a comment
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # Get the comment object
    comment.likes += 1  # Increment likes
    comment.save()  # Save the comment with updated like count
    messages.success(request, 'You liked this comment!')  # Success message
    return redirect('blog-detail', pk=comment.post.id)  # Redirect to the post detail view


# Dislike a comment
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # Get the comment object
    comment.dislikes += 1  # Increment dislikes
    comment.save()  # Save the comment with updated dislike count
    messages.success(request, 'You disliked this comment!')  # Success message
    return redirect('blog-detail', pk=comment.post.id)  # Redirect to the post detail view


def reply_comment(request, comment_id):
    parent_comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            new_comment = Comment(
                content=content,
                author=request.user,
                post=parent_comment.post,
                parent=parent_comment
            )
            new_comment.save()
            
            # Create a notification for the original comment's author
            if parent_comment.author != request.user:  # Avoid notifying the reply author
                Notification.objects.create(
                    user=parent_comment.author,
                    message=f"{request.user.username} replied to your comment: '{parent_comment.content}'",
                    comment=parent_comment
                )

            messages.success(request, 'Your reply has been posted!')
            return redirect('blog-detail', pk=parent_comment.post.id)
    
    return redirect('blog-detail', pk=parent_comment.post.id)


@login_required
def notifications_view(request):
    # Fetch all notifications for the logged-in user, ordered by creation date
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    # Calculate the unread notifications count
    unread_count = notifications.filter(is_read=False).count()  # Count of unread notifications

    # Optionally, mark notifications as read
    notifications.update(is_read=True)  # Mark all as read when accessing here
    
    # Pass notifications and unread_count to the template
    return render(request, 'blog/notifications.html', {
        'notifications': notifications,
        'unread_count': unread_count,  # Pass the unread count to the template
    })


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()  # Delete the notification
    messages.success(request, 'Notification deleted successfully.')  # A success message
    return redirect('notifications')  # Redirect back to notifications
