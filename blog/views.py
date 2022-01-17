from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import BlogPost, Comment
# from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required


def view_blog(request):
    """Redirect to blog page"""

    posts = BlogPost.objects.all()
    template = "blog/blog.html"
    context = {
        "posts": posts,
    }

    return render(request,
                  template,
                  context)
