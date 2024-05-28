from django.shortcuts import render
from products.models import Product, Category, Tag, ProductImage
from django.db.models import Q


def index(request):

    query = None
    categories = Category.objects.all()
    tags = Tag.objects.all()

    template = 'home/index.html'
    context = {
        
    }
    if request.GET:
        query = request.GET.get('search-input')
        promo = request.GET.get('promo-input')
        if query:
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(category__friendly_name__icontains=query) |
                    Q(tags__friendly_name__icontains=query)
                ).distinct()
                
                context = {
                    'products': products,
                    'categories': categories,
                    'tags': tags,
                    'query': query,
                }
                template = 'products/products_view.html'
        if promo:
                products = Product.objects.filter(is_featured=True)
                context= {
                    'products': products
                }
                template = 'products/products_view.html'
    return render(request, template, context)
