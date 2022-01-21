from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.


def index(request):
    """ view to return index page """

    blog_posts = BlogPost.objects.all()

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'home/index.html', context)
