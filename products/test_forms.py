from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.forms import ProductForm, ProductReviewForm
from products.models import Product, Category, Brand


class TestProductForms(TestCase):
    """Testing Product forms"""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='test_category'
        )
        self.brand = Brand.objects.create(
            name='test_brand'
        )
        self.product = Product.objects.create(
            name="Test product",
            description="test description",
            price="1200",
            category=self.category,
            brand=self.brand,
        )
        self.user = User.objects.create_user(
            username='test_user',
            email='test@test.com',
            password='testpassword'
        )

    def test_product_form_valid(self):
        """Testing valid product form"""

        form = ProductForm(
            {
                'name': 'Test product',
                'description': 'test description',
                'price': 1200,
                'category': self.category,
                'brand': self.brand,
            }
        )
        self.assertTrue(form.is_valid())
    
    def test_product_form_invalid(self):
        """Testing invalid product form"""

        form = ProductForm(
            {
                'name': '',
                'description': '',
                'price': '',
                'category': self.category,
                'brand': self.brand,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(form.errors['description'][0], 'This field is required.')
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_review_form(self):
        """Testing valid review form"""

        self.client.login(username='test_user', password='testpassword')

        form = ProductReviewForm(
            {
                'product': self.product,
                'user': self.user,
                'review_rating': 5,
                'review_text': "test review",
            }
        )
        self.assertTrue(form.is_valid())

    def test_product_review_form(self):
        """Testing invalid review form"""

        self.client.login(username='test_user', password='testpassword')

        form = ProductReviewForm(
            {
                'product': self.product,
                'user': self.user,
                'review_rating': "",
                'review_text': "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['review_rating'][0], 'This field is required.')
        self.assertEqual(form.errors['review_text'][0], 'This field is required.')