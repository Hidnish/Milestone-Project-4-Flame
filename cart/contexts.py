from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)

    if delivery_cost < settings.STANDARD_DELIVERY_COST_MIN:
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
