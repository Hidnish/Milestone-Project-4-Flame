
from django.test import TestCase
from contact.forms import MessageForm


class TestContactForms(TestCase):
    """Testing Contacts forms"""

    def test_message_form_invalid(self):
        form = MessageForm(
            {
                'name': 'test name',
                'email': 'test@test.com',
                'subject': 'test subject',
                'message': ' ',
            }
        )
        self.assertFalse(form.is_valid())

    def test_message_form_valid(self):
        form = MessageForm(
            {
                'name': 'test name',
                'email': 'test@test.com',
                'subject': 'test subject',
                'message': 'hello',
            }
        )
        self.assertTrue(form.is_valid())
