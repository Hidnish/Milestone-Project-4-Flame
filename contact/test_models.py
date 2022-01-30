from django.test import TestCase
from contact.models import Message


class TestContact(TestCase):
    """Testing Contact models"""

    def test_message_model(self):
        message = Message.objects.create(
            email="test@test.com",
            subject="test subject",
            message="test message",
        )
        self.assertEqual(str(message), message.subject)
