from django.test import TestCase
from profiles.forms import UserProfileForm


class TestProfileForms(TestCase):
    """Test Profile forms"""

    def test_profile_form(self):
        """Test Profile form only with required fields"""
        form = UserProfileForm(
            {
                'default_phone_number': '01234567890',
                'default_street_address1': 'test street',
                'default_street_address2': '',
                'default_town_or_city': 'test city',
                'default_county': '',
                'default_postcode': '12345',
                'default_country': 'SE',
            }
        )
        self.assertTrue(form.is_valid())
