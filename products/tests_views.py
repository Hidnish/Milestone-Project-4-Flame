from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Product, Category, Brand


class TestProductsViews(TestCase):
    """Test the Product views for all types of user"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user',
            email='test@test.com',
            password='testpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.brand = Brand.objects.create(
            name="test_brand",
            friendly_name="Test Brand"
        )
        self.product = Product.objects.create(
            code="123",
            name="test product",
            description="test description",
            price=1200,
            image="testimg.jpg",
            category=self.category,
        )
        self.all_products = reverse("products")
        self.product_detail = reverse("product_detail",
                                      kwargs={"product_id": self.product.id})

        # Views with superuser restrictions

        self.super_user = User.objects.create_superuser(
            username='test_admin',
            email='testadmin@test.com',
            password='testadminpassword'
        )

        self.add_product = reverse("add_product")
        self.home = reverse("home")
        self.edit_product = reverse("edit_product",
                                    kwargs={"product_id": self.product.id})
        self.delete_product = reverse("delete_product",
                                      kwargs={"product_id": self.product.id})

    def test_all_products_view(self):
        """
        Test the all products view
        """

        response = self.client.get(self.all_products)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertTemplateUsed(response, "base.html")

    def test_all_products_views_with_search(self):
        """
        Test the all_products view with a search query parameter 
        """

        response = self.client.get(self.all_products,
                                   {"q": "test"})
        context = response.context
        self.assertTrue(context['search_term'])
        self.assertEqual(context['search_term'], 'test')

    def test_all_products_views_with_blank_query(self):
        """ Test the all_products view with a blank query """

        response = self.client.get(self.all_products,
                                   {"q": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You did not enter any search criteria!')

    def test_all_products_views_with_category(self):
        """ Test the all_products view with a category parameter """

        response = self.client.get(self.all_products,
                                   {"category": "test_category"})
        category = Category.objects.get(name="test_category")
        context = response.context
        self.assertTrue(context['current_category'])
        self.assertEqual(context['current_category'], category)

    def test_all_products_views_with_brand(self):
        """ Test the all_products view with a brand parameter """

        response = self.client.get(self.all_products,
                                   {"brand": "test_brand"})
        brand = Brand.objects.get(name="test_brand")
        context = response.context
        self.assertTrue(context['current_brand'])
        self.assertEqual(context['current_brand'], brand)

    def test_all_products_views_with_sort(self):
        """ Test the all products view sorting by name """

        response = self.client.get(self.all_products,
                                   {"sort": "name"})
        context = response.context
        self.assertTrue(context['current_sorting'])
        self.assertEqual(context['current_sorting'], "name_None")

    def test_all_products_views_with_direction(self):
        """ Test the all products view with a direction parameter """

        response = self.client.get(self.all_products,
                                   {"sort": "name",
                                    "direction": "desc"})
        context = response.context
        self.assertTrue(context['current_sorting'])
        self.assertEqual(context['current_sorting'], "name_desc")

    def test_view_product_detail_view(self):
        """ Test the product_detail view """

        response = self.client.get(self.product_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertTemplateUsed(response, "base.html")

    # Views with user/superuser restrictions

    def test_add_product_not_superuser(self):
        """ Test the add_product view if the user is not a superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.add_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_add_product_superuser_GET(self):
        """ Test the add_product GET functionality for superusers """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.add_product)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")
        self.assertTemplateUsed(response, "base.html")

    def test_add_product_invalidform_POST(self):
        """ Test the add_product view using an invalid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.add_product, {
            "category": self.category,
            "brand": self.brand,
            "code": "",
            "name": "",
            "description": "",
            "price": "",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Failed to add product.\
 Please ensure the form is valid')

    def test_add_product_validform_POST(self):
        """ Test the add_product view with a valid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.add_product, {
            "name": "Test product",
            "description": "test description",
            "price": 1200,
        })
        product = Product.objects.get(name="Test product")
        self.assertTrue(product)
        self.assertEqual(product.description, "test description")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Product uploaded successfully!')

    def test_edit_product_not_superuser(self):
        """ Test the edit_product view if the user is not a superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.edit_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_edit_product_superuser_GET(self):
        """ Test the edit_product GET functionality if superuser """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.edit_product)
        self.assertEqual(response.context['form'].initial['name'],
                         self.product.name)
        self.assertEqual(response.context['form'].initial['description'],
                         self.product.description)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")
        self.assertTemplateUsed(response, "base.html")

    def test_edit_product_invalidform_POST(self):
        """ Test the edit_product view post with an invalid form"""

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.edit_product, {
            "name": "",
            "description": "",
            "price": "",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Failed to update product.\
 Please ensure the form is valid.')

    def test_edit_product_validform_POST(self):
        """ Test edit_product view with a valid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.edit_product, {
            "name": "Test edited product",
            "description": "test edited description",
            "price": 1300,
        }
        )
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.description, 'test edited description')
        self.assertEqual(product.price, 1300)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Successfully updated product!')

    def test_delete_product_not_superuser(self):
        """ Test delete_product view if user is not superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.delete_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, only store owners can do that')

    def test_delete_post_superuser_GET(self):
        """ Test delete_product view GET functionality if a superuser """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.delete_product)
        self.assertRedirects(response, self.all_products)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Product deleted!')
