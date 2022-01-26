from django.test import TestCase
from products.models import Category, Product, Brand, ProductReview
from django.contrib.auth.models import User


class TestProductsModels(TestCase):

    def test_category_model(self):
        category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        self.assertEqual(str(category), "test_category")

    def test_brand_model(self):
        brand = Brand.objects.create(
            name="test_brand",
            friendly_name="Test Brand",
        )
        self.assertEqual(str(brand), "test_brand")

    def test_product_model(self):
        category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        brand = Brand.objects.create(
            name="test_brand",
            friendly_name="Test Brand",
        )
        product = Product.objects.create(
            code="1",
            name="Test product",
            description="test description",
            price="1200",
            image="testimg.jpg",
            category=category,
            brand=brand
        )
        self.assertEqual(str(product), "Test product")

    def test_product_review_model(self):
        product = Product.objects.create(
            name="Test Product",
            description="test description",
            price="1200",
        )
        user = User.objects.create_user(
            username='test_user',
            email='test@test.com',
            password='testpassword'
        )
        product_review = ProductReview.objects.create(
            product=product,
            user=user,
            review_text="test review",
            review_rating=5,
        )

        self.assertEqual(str(product_review), product_review.product.name)
