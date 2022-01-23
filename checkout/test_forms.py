from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_form_only_required_fields(self):
        """
        Test form with only required fields filled in
        """
        form = OrderForm(
            {
                'full_name': 'Test Testy',
                'email': 'test@test.com',
                'phone_number': '01234567890',
                'postcode': '',
                'town_or_city': 'Paris',
                'street_address1': '123 Street',
                'street_address2': '',
                'county': '',
                'country': 'SE'
            }
        )
        self.assertTrue(form.is_valid())

    def test_order_form_without_required_fields(self):
        """
        Test form with blank required fields
        """
        form = OrderForm(
            {
                'full_name': '',
                'email': '',
                'phone_number': '',
                'town_or_city': '',
                'street_address1': '',
                'country': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')
