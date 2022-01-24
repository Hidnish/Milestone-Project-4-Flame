from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import BlogPost, Comment
from .forms import CommentForm, BlogPostForm

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def view_blog(request):
    """view to return blog page"""

    posts = BlogPost.objects.all()
    template = "blog/blog.html"
    context = {
        "posts": posts,
    }

    return render(request,
                  template,
                  context)


def view_blog_post(request, post_id):
    """view to return blog post details"""

    blog_post = get_object_or_404(BlogPost, pk=post_id)
    comments = Comment.objects.filter(post=blog_post).order_by('-date')
    form = CommentForm()

    template = "blog/blog_post.html"

    context = {
        "comment_form": form,
        "post": blog_post,
        "comments": comments,
    }

    return render(request,
                  template,
                  context)


@login_required
def save_comment(request, post_id):
    """Save comment on Blog post"""

    post = BlogPost.objects.get(pk=post_id)
    user = request.user
    Comment.objects.create(
        user=user,
        post=post,
        comment=request.POST['comment'],
    )

    data = {
        'user': user.username,
        'comment': request.POST['comment'],
    }

    return JsonResponse({'bool': True, 'data': data})


@login_required
def delete_comment(request, comment_id):
    """Remove specific comment"""

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
        messages.info(request, 'Comment deleted!')
        return redirect(reverse('view_blog_post', args=[comment.post.id]))
    else:
        messages.error(
            request,
            "Only store owner and the commentator can do that."
        )
        return redirect(reverse('view_blog_post', args=[comment.post.id]))


@login_required
def delete_last_comment(request, post_id, user_id):
    """
    Remove last comment added by specific user via JS, without refreshing page
    """

    last_comment_by_user = Comment.objects.filter(
        post=post_id, user=user_id).order_by('-date')[0]
    
    if request.user == last_comment_by_user.user or request.user.is_superuser:
        last_comment_by_user.delete()
        return JsonResponse({'bool': True})
    else: 
        messages.error(
            request,
            "Only store owner and the commentator can do that."
        )
        return redirect(reverse('view_blog_post', args=[post_id]))


@login_required
def add_blog_post(request):
    """
    Allow superusers to add a new blog post
    from the website
    """

    if request.user.is_superuser:
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Post has been added to the Blog.")
                return redirect(reverse("view_blog_post", args=[post.id]))
            else:
                messages.error(request,
                               "Failed to add the post. \
                                Please check the form inputs \
                                are correct and try again.")
        else:
            form = BlogPostForm()
    else:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse("view_blog"))

    template = "blog/add_blog_post.html"

    context = {
        "form": form,
        "dont_show_checkout": True,
    }

    return render(request,
                  template,
                  context)


@login_required
def edit_blog_post(request, post_id):
    """
    Allow superusers to edit a specific blog post
    from the website front-end
    """

    if request.user.is_superuser:
        post = get_object_or_404(BlogPost, pk=post_id)
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 "Post updated")
                return redirect(reverse("view_blog_post", args=[post.id]))
            else:
                messages.error(request,
                               "Failed to edit the post. \
                                Please check the form inputs \
                                are correct and try again.")
        else:
            form = BlogPostForm(instance=post)
    else:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse("view_blog"))

    template = "blog/edit_blog_post.html"
    context = {
        "form": form,
        "post": post,
        "edit_post": True,
        "dont_show_checkout": True,
    }

    return render(request,
                  template,
                  context)


@login_required
def delete_blog_post(request, post_id):
    """
    Allow superusers to delete a specific blog post
    from the website front-end
    """

    if request.user.is_superuser:
        post = get_object_or_404(BlogPost, pk=post_id)
        post.delete()
        messages.info(request, "Post deleted")
        return redirect(reverse("view_blog"))
    else:
        messages.error(request, "Sorry, only store owners can do that")
        return redirect(reverse("view_blog"))
