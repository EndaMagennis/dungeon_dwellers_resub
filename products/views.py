from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Tag


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

