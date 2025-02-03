from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from .forms import CommentForm, CollaborateForm
from django.db.models import Q
from .models import Post, Comment, Notification, Category


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

    This view fetches and displays all posts ordered by the date they were
    posted, with additional support for search functionality. It also includes
    trending posts in the context for additional user engagement.

    Attributes:
        model (Post): The Django model to be used for this view, representing
        the blog posts. template_name (str): The template filename that will
        render the output of this view (e.g., 'blog/welcome.html').
        context_object_name (str): The name of the context variable that will
        contain the list of blog articles. ordering (list): A list defining the
        order in which to return articles, with the most recent posts first.
        paginate_by (int): Number of articles displayed per page for
        pagination.

    Methods:
        get_queryset():
            Returns a queryset of blog posts, optionally filtered by a search
            query found in the URL.

        get_context_data(**kwargs):
            Extends the default context data by adding a list of trending posts
            to provide additional context and user engagement opportunities.

    Usage:
        The view can be accessed through a URL configuration and will
        automatically handle pagination and search queries based on user
        input from the request.
    """
    model = Post
    template_name = 'blog/welcome.html'
    context_object_name = 'articles'
    ordering = ["-date_posted"]
    paginate_by = 8

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date_posted')
        search_query = self.request.GET.get('search', '')
        category_query = self.request.GET.get('category')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        if category_query:
            queryset = queryset.filter(category__name__iexact=category_query)

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
        context['trending_posts'] = Post.objects.order_by('?')[:5]

        # Only get unread notification count for authenticated users
        if self.request.user.is_authenticated:
            context['unread_count'] = Notification.objects.filter(
                user=self.request.user,
                is_read=False
            ).count()
        else:
            context['unread_count'] = 0

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
        context_object_name (str): The name used to reference the specific post
        in the template.

    Methods:
        get_context_data(**kwargs): Adds comments and trending posts to the
        context. post(request, *args, **kwargs):
        Handles form submissions for new comments.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = self.object.comments.filter(
            parent__isnull=True
        ).order_by('-created_at')

        # Set up pagination for comments
        paginator = Paginator(comments, 6)
        page_number = self.request.GET.get('page')
        page_comments = paginator.get_page(page_number)

        # Add to context
        context['comments'] = page_comments
        context['trending_posts'] = Post.objects.order_by('?')[:5]
        context['comment_form'] = CommentForm()
        context['paginator'] = paginator

        context['category'] = Category.objects.all()

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
            HttpResponse: Redirects to the post detail page if successful or
            renders the same page with form errors.
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

    This view is accessible only to authenticated users. Upon successful form
    submission, it assigns the current user as the author of the post and
    displays a success message.

    Attributes:
        model: The database model to use (Post).
        fields: The fields to be included in the form ('title' and 'content').
        success_url: The URL to redirect to after successful creation.

    Methods:
        form_valid(form): Assigns the request user as the author of the post
                          and calls the parent's form_valid method.
    """
    model = Post
    fields = ['title', 'content', 'category']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'Your post has been created successfully!'
        )
        return super().form_valid(form)


# Update existing post view with permissions check
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to update an existing post.

    This view requires the user to be logged in and ensures that only the
    author of the post can make changes. On successful form submission,
    it updates the post and retains the author as the current user.

    Attributes:
        model: The database model to use (Post).
        fields: The fields to be included in the form ('title' and 'content').
        success_url: The URL to redirect to after successful update
        (will be overridden).

    Methods:
        form_valid(form): Assigns the request user as the author of the post
                          and calls the parent's form_valid method.
        get_success_url(): Returns the URL to redirect to after successful
        update.
        test_func(): Checks if the current user is the author of the post,
                     returning True if so, otherwise False.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(
            self.request,
            'Your post has been updated successfully!'
        )
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to the detail view of the updated post."""
        return reverse('blog-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


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
        delete(request, *args, **kwargs): Handles the deletion of the post and
        sets a success message.
        test_func(): Checks if the current user is the author of the post,
                     returning True if so, otherwise False.
    """
    model = Post
    success_url = reverse_lazy('welcome')

    def delete(self, request, *args, **kwargs):
        """Handle the deletion of the post and notify the user."""
        post = self.get_object()  # Get the post object

        # Capture the current category and search parameters
        current_category = request.GET.get('category', '')
        search_query = request.GET.get('search', '')

        post.delete()
        messages.success(request, 'Your post has been deleted!')

        redirect_url = (
            f"{self.success_url}?category={current_category}"
            f"&search={search_query}"
        )
        return redirect(redirect_url)


# Update a comment by the author; only authorized users can edit.
def update_comment(request, comment_id):
    """
    Update a specific comment.

    Ensures that the logged-in user is the author of the comment before
    allowing edits. If the user is authorized and submits valid content,
    the comment is updated, and a success message is displayed.

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
        messages.error(
            request,
            "You do not have permission to edit this comment."
        )
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

    This function checks if the logged-in user is the author of the comment
    before allowing deletion. If authorized, the comment is deleted, and
    a success message is displayed. Otherwise, an error message is shown.

    Parameters:
        request: The HTTP request object.
        comment_id: The ID of the comment to be deleted.

    Returns:
        Redirects to the blog detail page after deletion or shows an error
        message if permission is denied.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect('blog-detail', pk=post_id)
    else:
        messages.error(
            request,
            "You do not have permission to delete this comment."
        )
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
    If the form is valid, the request is saved and a success message is
    displayed.

    Parameters:
        request: The HTTP request object.

    Returns:
        Redirects to the support and collaboration page on successful form
        submission or re-renders the page with the form if there are validation
        errors.
    """
    collaborate_form = CollaborateForm()

    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                'Your request has been submitted successfully!'
            )
            return redirect('support-and-collaboration')

    return render(
        request, 'blog/support_and_collaboration.html',
        {'collaborate_form': collaborate_form}
    )


# Like a post
def like_post(request, post_id):
    """
    Like a specific post.

    Increments the like count of the post specified by post_id. Upon
    successfully liking the post, a success message is displayed,
    and the user is redirected to the detail view of the post.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post to be liked.

    Returns:
        HttpResponse: Redirects to the blog detail view for the specified post.
    """
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    messages.success(request, 'You liked this post!')
    return redirect('blog-detail', pk=post_id)


# Dislike a post
def dislike_post(request, post_id):
    """
    Dislike a specific post.

    Increments the dislike count of the post specified by post_id. Upon
    successfully disliking the post, a success message is displayed, and
    the user is redirected to the detail view of the post.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post to be disliked.

    Returns:
        HttpResponse: Redirects to the blog detail view for the specified post.
    """
    post = get_object_or_404(Post, id=post_id)
    post.dislikes += 1
    post.save()
    messages.success(request, 'You disliked this post!')
    return redirect('blog-detail', pk=post_id)


# Like a comment
def like_comment(request, comment_id):
    """
    Like a specific comment.

    Increments the like count for the comment specified by comment_id. Upon
    successfully liking the comment, a success message is displayed, and
    the user is redirected to the detail view of the associated post.

    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to like.

    Returns:
        HttpResponse: Redirects to the blog detail view for the associated
        post.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()
    messages.success(request, 'You liked this comment!')
    return redirect('blog-detail', pk=comment.post.id)


# Dislike a comment
def dislike_comment(request, comment_id):
    """
    Dislike a specific comment.

    Increments the dislike count for the comment specified by comment_id. Upon
    successfully disliking the comment, a success message is displayed, and
    the user is redirected to the detail view of the associated post.

    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to dislike.

    Returns:
        HttpResponse: Redirects to the blog detail view for the associated
        post.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.dislikes += 1
    comment.save()
    messages.success(request, 'You disliked this comment!')
    return redirect('blog-detail', pk=comment.post.id)


def reply_comment(request, comment_id):
    """
    Reply to a specific comment.

    Allows the logged-in user to submit a reply to the comment identified by
    comment_id. If the form is submitted successfully, a new comment is
    created linking it to the parent comment,and a notification is sent to the
    original comment's author.

    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment being replied to.

    Returns:
        HttpResponse: Redirects to the blog detail view for the associated
        post.
    """
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
            if parent_comment.author != request.user:
                Notification.objects.create(
                    user=parent_comment.author,
                    message=(
                        f"{request.user.username} replied to your comment: "
                        f"'{parent_comment.content}'"
                    ),
                    comment=parent_comment
                )

            messages.success(request, 'Your reply has been posted!')
            return redirect('blog-detail', pk=parent_comment.post.id)

    return redirect('blog-detail', pk=parent_comment.post.id)


@login_required
def notifications_view(request):
    """
    View to display user notifications.

    Fetches and displays notifications for the logged-in user, ordered by
    creation date. Also marks all notifications as read.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the notifications page, passing the notifications
        and unread count to the template.
    """

    notifications = (
        Notification.objects
        .filter(user=request.user)
        .order_by('-created_at')
    )

    unread_count = notifications.filter(is_read=False).count()

    notifications.update(is_read=True)

    # Pass notifications and unread_count to the template
    return render(request, 'blog/notifications.html', {
        'notifications': notifications,
        'unread_count': unread_count,
    })


@login_required
def delete_notification(request, notification_id):
    """
    Delete a specific notification.

    Retrieves the notification specified by notification_id and deletes it if
    it belongs to the logged-in user. A success message is displayed after
    deletion.

    Args:
        request: The HTTP request object.
        notification_id: The ID of the notification to delete.

    Returns:
        HttpResponse: Redirects to the notifications view after deletion.
    """
    notification = get_object_or_404(
        Notification,
        id=notification_id,
        user=request.user
    )
    notification.delete()
    messages.success(request, 'Notification deleted successfully.')
    return redirect('notifications')
