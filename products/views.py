from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ view to return products, plus sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ view to to show individial product details """

    product = get_object_or_404(Product, pk=product_id)
    product_category = product.category.name
    related_products = Product.objects.filter(category__name=product_category)

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)
