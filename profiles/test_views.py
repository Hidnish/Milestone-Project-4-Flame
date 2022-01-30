from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from checkout.models import Order


class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.user_profile = reverse("profile")
        self.login = reverse("account_login")
        self.form = UserProfileForm

    def test_user_profile_signin_required(self):
        """
        Test to ensure the user needs to be signed in to
        see the userprofile page
        """

        response = self.client.get(self.user_profile)
        self.assertNotEqual(response.status_code, 200)

    def test_user_profile_page_signed_in(self):
        """ Test the user profile page when signed in """

        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.user_profile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertTemplateUsed(response, "base.html")

    def test_user_profile_invalid_form(self):
        """ Test invalid form """

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.user_profile, {
            "default_postcode": "122122121212121212121212121212"}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Update failed, please ensure \
                                     the form is valid')

    def test_user_profile_valid_form(self):
        """ Test valid from """

        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.user_profile, {
            "default_phone_number ": "123123123",
            "default_street_address_1": "test address",
            "default_street_address_2": "test address 2",
            "default_town_or_city": "test city",
            "default_county": "SE",
            "default_postcode": "12345"}
        )
        form = self.form(response, instance=self.user)
        self.assertTrue(form.is_valid())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Profile updated successfully')

    def test_previous_orders_view(self):
        """ Test previous orders view with logged in user """

        self.client.login(username="testuser", password="testpassword")
        user_profile = UserProfile.objects.get(user=self.user)

        order = Order.objects.create(user_profile=user_profile)

        response = self.client.get(
            reverse("order_history",
                    kwargs={"order_number": order.order_number}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
        self.assertTemplateUsed(response, "base.html")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         f'This is a past confirmation for order number \
        {order.order_number}. A confirmation was sent on the order date.')


