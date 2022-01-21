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

        placeholders = {
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'radius-10'
            self.fields[field].label = False
