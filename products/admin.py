from django.contrib import admin
from .models import Product, Category, Brand

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('code', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
