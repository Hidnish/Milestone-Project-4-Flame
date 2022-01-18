from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import BlogPost, Comment
from .forms import CommentForm

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
    comment.delete()
    messages.info(request, 'Review deleted!')

    return redirect(reverse('view_blog_post', args=[comment.post.id]))


def delete_last_comment(request, post_id):
    """
    Remove last comment added via JS without refreshing page
    """

    last_comment = Comment.objects.filter(post=post_id).order_by('-date')[0]
    last_comment.delete()

    return JsonResponse({'bool': True})
