from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from products.models import Product


class TestCartViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_page = reverse("home")
        self.view_cart = reverse("view_cart")
        self.item = Product.objects.create(name="test-item", price="1")
        self.add_to_cart = reverse("add_to_cart",
                                   kwargs={"item_id": self.item.id})
        self.adjust_cart = reverse("adjust_cart",
                                   kwargs={"item_id": self.item.id})
        self.remove_from_cart = reverse("remove_from_cart",
                                        kwargs={"item_id": self.item.id})

    def test_view_cart_view(self):
        """
        Test the view_cart page
        """

        response = self.client.get(self.view_cart)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertTemplateUsed(response, "base.html")

    def test_add_to_cart(self):
        """
        Test that the context updates when an item
        is added to the cart +
        If the item is added a second time the quantity
        updates accordingly
        """

        response = self.client.post(self.add_to_cart,
                                    data={"quantity": "1",
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Added {self.item.name} to your cart')

        response = self.client.post(self.view_cart)
        context = response.context
        self.assertEqual(context["cart_items"][0]["item_id"],
                         f"{self.item.id}")

        # Test if adding an item already present in the cart updates
        # the quantity
        response = self.client.post(self.add_to_cart,
                                    data={"quantity": 3,
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Updated {self.item.name} quantity to 4')

    def test_adjust_cart(self):
        """
        Test if the cart is updated when a item quantity is increased/reduced
        and if the quantity is set to 0 the item is removed
        """

        response = self.client.post(self.adjust_cart,
                                    data={"quantity": 4})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Updated {self.item.name} quantity to 4')
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertEqual(context["cart_items"][0]["quantity"], 4)

        # Test to ensure cart empties when quantity set to 0
        response = self.client.post(self.adjust_cart,
                                    data={"quantity": 0})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Removed {self.item.name} from your cart')
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertEqual(context["cart_items"], [])

    def test_remove_from_cart(self):
        """
        Test that the items are removed from the cart
        """

        # Add product to be removed
        self.client.post(self.adjust_cart,
                         data={"quantity": 1})

        # Remove item
        response = self.client.post(self.remove_from_cart)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         f'Removed {self.item.name} from your cart')

        # Ensure item has been removed from context
        response = self.client.post(self.view_cart)
        context = response.context
        self.assertEqual(context["cart_items"], [])
