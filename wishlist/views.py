from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Wishlist
from products.models import Product

class WishlistView(View):
    """View for user wishlist"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlist = get_object_or_404(Wishlist, user=request.user)
            products = wishlist.get_products()
            context = {
                'wishlist': wishlist,
                'products': products,
            }
            return render(request, 'wishlist/wishlist.html', context)
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