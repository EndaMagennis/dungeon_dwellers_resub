from django.views import View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from .models import Product,Category, Tag, ProductImage
from wishlist.models import Wishlist
from .forms import ProductForm
from django.contrib import messages


class ProductListView(View):
    """ A view to return the home page """
    
    def get(self, request, *args, **kwargs):
        # Get the user's wishlist if they are logged in
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=request.user)
        else:
            wishlist = None
        # Get all products and paginate them
        p = Paginator(Product.objects.all(), 10)
        page = request.GET.get('page')
        products = p.get_page(page)
        query = None

        categories = Category.objects.all()
        tags = Tag.objects.all()

        template = 'products/products_view.html'

        # If the user has searched for a product
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
            # If the user has searched for a product that is on sale
            if promo:
                products = Product.objects.filter(is_featured=True)

                context= {
                    'products': products
                }

        context = {
            'products': products,
            'categories': categories,
            'tags': tags,
            'wishlist': wishlist,
        }

        return render(request, template, context)


class ProductDetailView(View):

    """A view of an individual product in more detail"""

    def get(self, request, product_id, *args, **kwargs):

        query = None
        categories = Category.objects.all()
        tags = Tag.objects.all()

        product = get_object_or_404(Product, id=product_id)
        
        images = ProductImage.objects.filter(
            product = product,
        )
        template = 'products/product_detail.html'

        context = {
            'product': product,
            'images' : images
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


class ProductAddView(View):

    def get(self, request, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        product_form = ProductForm()

        context = {
            'product_form': product_form,
        }
        return render(request, 'products/product_add.html', context)

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(instance=ProductImage)
        if request.method == 'POST':
            product_form = ProductForm(request.POST)
            images = request.FILES.getlist('images')
            if product_form.is_valid():
                product = product_form.save()
                for i in images:
                    ProductImage(product=product, image=i).save()
                return redirect('products')
            context = {
                'product_form': product_form,
            }
            return render(request, 'products/product_add.html', context)
        return redirect('products')


class ProductEditView(View):
 
    def get(self, request, product_id, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))
        
        product = get_object_or_404(Product, pk=product_id)
        product_form = ProductForm(instance=product)

        context = {
            'product': product,
            'product_form': product_form
        }

        return render(request, 'products/product_edit.html', context)


    def post(self, request, product_id, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            product_form = ProductForm(request.POST, request.FILES, instance=product)
            images = request.FILES.getlist('images')
            if product_form.is_valid():
                product = product_form.save()
                for i in images:
                    ProductImage(product=product, image=i).save()
                messages.success(request, 'Successfully updated product!')
                return redirect('products')
            else:
                messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        else:
            product_form = ProductForm(instance=product)
            context = {
                'product_form': product_form,
                'product': product,
                'images': images
            }
            return render(request, 'products/product_edit.html', context)

        return redirect('products')


class ProductDeleteView(DeleteView):
    """View for deleting a product"""
    def get(self, request, product_id, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))
    
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))



class ProductImageAddView(View):

    def get(self, request, product_id, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        product = get_object_or_404(Product, pk=product_id)
        product_image = ProductImage()
        
        context = {
            'product': product,
            'product_image': product_image,
        }

        template = 'products/product_image_add.html'

        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        image_form = ProductForm(request.POST, request.FILES)
        if image_form.is_valid():
            product = request.POST.get('product')
            image = request.FILES.get('image')
            image = ProductImage(image=image)
            image.product = product
            image.save()
            return redirect('products')
        context = {
            'image_form': image_form,
        }
        return render(request, 'products/products.html', context)
