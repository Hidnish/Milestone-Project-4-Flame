from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name="blog"),
    path('<int:post_id>/', views.view_blog_post, name="blog_post"),
]