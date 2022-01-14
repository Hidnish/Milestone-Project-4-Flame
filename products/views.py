from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

from .models import Product, Category, Brand, ProductReview
from .forms import ProductForm, ProductReviewForm

from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.


def all_products(request):
    """ view to return products, plus sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    brand = None
    category = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'brand':
                sortkey = 'brand__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            this_category = request.GET['category']
            products = products.filter(category__name=this_category)
            category = Category.objects.get(name=this_category)

        if 'brand' in request.GET:
            this_brand = request.GET['brand']
            products = products.filter(brand__name=this_brand)
            brand = Brand.objects.get(name=this_brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__name__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'current_category': category,
        'current_brand': brand,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ view to to show individial product details """

    product = get_object_or_404(Product, pk=product_id)
    product_category = product.category.name
    related_products = Product.objects.filter(category__name=product_category)
    review_form = ProductReviewForm()

    # Product reviews
    reviews = ProductReview.objects.filter(product=product)

    context = {
        'product': product,
        'related_products': related_products,
        'review_form': review_form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """Add a product to the store"""
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added Product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def save_review(request, product_id):
    """Save product reviews and ratings"""

    product = Product.objects.get(pk=product_id)
    user = request.user
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review_text=request.POST['review_text'],
        review_rating=request.POST['review_rating'],
    )

    data = {
        'user': user.username,
        'review_text': request.POST['review_text'],
        'review_rating': request.POST['review_rating']
    }

    return JsonResponse({'bool': True, 'data': data})
    # messages.success(request, 'Message successfully added!')
    # return redirect(reverse('product_detail', args=[product.id]))
