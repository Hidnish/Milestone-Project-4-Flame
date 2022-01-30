from django import forms
from .models import BlogPost, Comment
from products.widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = {
            "image",
            "body",
            "title",
        }

    field_order = ['title', 'body', 'image']

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["class"] = 'radius-10'
        self.fields["body"].widget.attrs["class"] = 'radius-10'
        self.fields["image"].widget.attrs["class"] = ' radius-10 new-image'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
