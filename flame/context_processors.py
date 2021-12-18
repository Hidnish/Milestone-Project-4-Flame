from products.models import Brand


# provide all pages with Brand objects to display brands in navbar dropdown 
def all_brands(request):
    return {'brands': Brand.objects.all()}
