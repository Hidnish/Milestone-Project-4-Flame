from django.contrib import admin
from .models import Product, Category, Brand

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_dispaly = (
        'code',
        'name',
        'description',
        'price',
        'image',
    )
    # has to be a tuple to order based on multiple columns 
    ordering = ('code', )

class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = (
        'name',
        'friendly_name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_dispaly = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)

