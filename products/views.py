from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Tag, ProductImage


class ProductListView(View):
    """ A view to return the home page """
    
    def get(self, request, *args, **kwargs):
        
        products = Product.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()

        context = {
            'products': products,
            'categories': categories,
            'tags': tags,
        }

        return render(request, 'products/products_view.html', context)


class ProductDetailView(View):
    """A view of an individual product in more detail"""

    def get(self, request, product_id, *args, **kwargs):

        product = get_object_or_404(Product, id=product_id)
        images = ProductImage.objects.filter(
            product = product,
        )

        context = {
            'product': product,
            'images' : images
        }

        return render(request, 'products/product_detail.html', context)