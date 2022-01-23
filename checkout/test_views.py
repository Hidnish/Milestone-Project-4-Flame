from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testPassword'
        )
        self.product = Product.objects.create(name="test-product", price="1")
        self.checkout = reverse("checkout")
        self.add_to_cart = reverse("add_to_cart",
                                   kwargs={"item_id": self.product.id})

    def test_checkout_view_with_empty_cart(self):
        """ Test the checkout view with an empty cart. """

        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "The cart is empty at the moment")

    def test_checkout_view_with_cart(self):
        """ Test the checkout view with a product in the cart """

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")
        self.assertTemplateUsed(response, "base.html")

    def test_checkout_success(self):
        """ Test the checkout_success view. """

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        response = self.client.post(self.checkout,
                                    data={
                                        'full_name': 'testuser',
                                        'email': 'test@test.com',
                                        'phone_number': '1234567890',
                                        'street_address1': 'test street',
                                        'street_address2': '',
                                        'town_or_city': 'testCity',
                                        'county': 'testCountry',
                                        'country': 'SE',
                                        'postcode': '',
                                        'client_secret': 'client',
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def test_checkout_view_with_form_prefilled(self):
        """
        Test the checkout view form is prefilled
        with the user data
        """

        self.client.post(self.add_to_cart,
                         data={"quantity": "1",
                               "redirect_url": "/"})
        self.client.login(username="testuser", password="testPassword")
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['order_form'].initial['email'],
                         self.user.email)
