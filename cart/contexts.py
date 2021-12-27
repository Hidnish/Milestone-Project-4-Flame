from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
        })

    delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)

    if not delivery_cost:
        home_delivery = 0
    elif delivery_cost < settings.STANDARD_DELIVERY_COST_MIN:
        home_delivery = settings.STANDARD_DELIVERY_COST_MIN
    elif delivery_cost > settings.STANDARD_DELIVERY_COST_MAX:
        home_delivery = settings.STANDARD_DELIVERY_COST_MAX
    else:
        home_delivery = delivery_cost

    grand_total = total + home_delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'home_delivery': home_delivery,
        'grand_total': grand_total
    }

    return context
