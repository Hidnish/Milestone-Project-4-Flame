from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name="view_blog"),
    path('<int:post_id>/', views.view_blog_post, name="view_blog_post"),
    path('save_comment/<int:post_id>/', views.save_comment, name="save_comment"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('delete_last_comment/<int:post_id>/', views.delete_last_comment, name="delete_last_comment"),
    path('add_blog_post/', views.add_blog_post, name="add_blog_post"),
    path('edit_blog_post/<int:post_id>/', views.edit_blog_post, name="edit_blog_post"),
    path('delete_blog_post/<int:post_id>/', views.delete_blog_post, name="delete_blog_post"),
]