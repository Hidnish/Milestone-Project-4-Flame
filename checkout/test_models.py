from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Product


class TestOrderModels(TestCase):
    """Test Checkout models"""

    def test_order_model(self):
        """Test Order Model"""

        order = Order.objects.create(
            full_name="Test Order",
        )

        self.assertEqual(str(order), order.order_number)

    def test_order_line_item_model(self):
        """Test OrderLineItem Model"""

        order = Order.objects.create(
            full_name="Test Order",
        )

        product = Product.objects.create(
            code='12345',
            name="Test product",
            price=1200,
        )

        order_line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            lineitem_total=1200,
        )

        self.assertEqual(
            str(order_line_item),
            f'Product code: {self.product.code} on order \
               {self.order.order_number}'
        )
