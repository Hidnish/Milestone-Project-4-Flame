from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Product, Category, Brand, ProductReview
from .forms import ProductForm, ProductReviewForm

from django.db.models import Avg
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
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(
                brand__name__icontains=query) | Q(category__name__icontains=query)
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

    # Product reviews and average
    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    avg_reviews = reviews.aggregate(avg_rating=Avg('review_rating'))

    context = {
        'product': product,
        'related_products': related_products,
        'review_form': review_form,
        'reviews': reviews,
        'avg_reviews': avg_reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product uploaded successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        "dont_show_checkout": True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        "dont_show_checkout": True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def save_review(request, product_id):
    """Save product reviews and ratings"""

    product = Product.objects.get(pk=product_id)
    user = request.user
    ProductReview.objects.create(
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

    avg_reviews = ProductReview.objects.filter(
        product=product).aggregate(avg_rating=Avg('review_rating'))

    return JsonResponse({'bool': True, 'data': data, 'avg_reviews': avg_reviews })


@login_required
def delete_review(request, review_id):
    """Remove specific review"""

    review = get_object_or_404(ProductReview, pk=review_id)
    review.delete()
    messages.info(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[review.product.id]))


def delete_last_review(request, product_id):
    """
    Remove last review added via JS without refreshing page
    """

    last_review = ProductReview.objects.filter(product=product_id).order_by('-date')[0]
    last_review.delete()

    return JsonResponse({'bool': True})
