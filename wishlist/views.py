from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .models import Wishlist
from products.models import Product, Tag, Category


class WishlistView(View):
    """View for user wishlist"""
    def get(self, request, *args, **kwargs):

        query = None
        categories = Category.objects.all()
        tags = Tag.objects.all()

        if request.user.is_authenticated:
            wishlist = get_object_or_404(Wishlist, user=request.user)
            products = wishlist.get_products()

            template = 'wishlist/wishlist.html'
            context = {
                'wishlist': wishlist,
                'products': products,
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
                    context = {
                        'products': products
                    }
                    template = 'products/products_view.html'

            return render(request, template, context)
        else:
            return render(request, 'account_login.html')


class AddRemoveWishlistView(View):
    """View for adding and removing products from wishlist"""
    def post(self, request, *args, **kwargs):
        ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if request.user.is_authenticated and ajax:
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=product_id)
            wishlist = get_object_or_404(Wishlist, user=request.user)
            if wishlist.add_to_wishlist(product):
                product_in_wishlist = True
                messages.success(request, 'Product added to wishlist')
            else:
                wishlist.remove_from_wishlist(product)
                product_in_wishlist = False
                messages.success(request, 'Product removed from wishlist')
            return JsonResponse(
                {
                    'success': True,
                    'product_in_wishlist': product_in_wishlist
                }
            )
        else:
            return render(request, 'account_login.html')
