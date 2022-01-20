from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form to allow users to contact the store owner
    """

    class Meta:
        model = Message
        fields = (
            'email',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'radius-10'
