from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category, Brand
from django.db.models import Q

# Create your views here.


def all_products(request):
    """ view to return products, plus sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter any search criteria!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__name__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)

    if 'category' in request.GET:
        category = request.GET['category']
        products = products.filter(category__name=category)
        # current_category = Category.objects.filter(name__in=category)

    if 'brand' in request.GET:
        this_brand = request.GET['brand']
        products = products.filter(brand__name=this_brand)

    context = {
        'products': products,
        'search_term': query,
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
