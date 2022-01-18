from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import BlogPost, Comment
# from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required


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

    post = get_object_or_404(BlogPost, pk=post_id)

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)

    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = post
    #         comment.save()

    #         return redirect('post_detail', slug=post.slug)
    # else:
    #     form = CommentForm()

    template = "blog/blog_post.html"

    context = {
        # "form": form,
        "post": post,
        # "comments": comments,
    }

    return render(request,
                  template,
                  context)
