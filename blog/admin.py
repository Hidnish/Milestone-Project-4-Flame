from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'author',
                    'date',)

    ordering = ('-date', )

class CommentAdmin(admin.ModelAdmin):

    list_display = ('post',
                    'user',
                    'date',)

    ordering = ('-date', )



admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
