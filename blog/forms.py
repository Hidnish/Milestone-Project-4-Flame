from django import forms
from .models import BlogPost, Comment
from products.widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = {
            "title",
            "body",
            "image",
        }

    image = forms.ImageField(
        label="Image",
        required=True,
        widget=CustomClearableFileInput,
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

