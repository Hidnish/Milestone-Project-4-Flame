from django.test import TestCase, Client
from django.contrib.messages import get_messages


class TestContactViews(TestCase):
    """Testing Contact Views"""

    def test_contact_view_GET(self):
        """
        Test the contact page to make sure it renders
        the desired template.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_view_valid_POST(self):
        """
        Tests contact view when method is POST and
        contact is valid
        """

        response = self.client.post('/contact/', {
            'email': 'test@test.com',
            'subject': 'test subject',
            'message': 'test message',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Thank you for your message,\
                              we will be in touch soon")

    def test_contact_view_invalid_POST(self):
        """
        Tests contact view when method is POST and
        contact is not valid
        """
        response = self.client.post('/contact/', {
            'email': 'test@test.com',
            'subject': '',
            'message': ''
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Something went wrong,\
                            Please try again")


