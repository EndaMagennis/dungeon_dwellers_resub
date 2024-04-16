from django.contrib import admin
from .models import Category, Tag, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
    search_fields = ['name', 'friendly_name']
    ordering = ['name']

    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
    search_fields = ['name', 'friendly_name']
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'category',
    )
    search_fields = ['name', 'category', 'tag']
    ordering = ['name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'image',
    )
    search_fields = ['product', 'image']
    ordering = ['product']
