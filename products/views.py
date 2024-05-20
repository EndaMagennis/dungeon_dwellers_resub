from django.views import View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import DeleteView
from .models import Product, Category, Tag, ProductImage
from .forms import ProductForm
from django.contrib import messages


class ProductListView(View):
    """ A view to return the home page """
    
    def get(self, request, *args, **kwargs):
        
        products = Product.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()

        template = 'products/products_view.html'

        if request.GET:
            query = request.GET.get('search-input')
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

        context = {
            'products': products,
            'categories': categories,
            'tags': tags,
        }

        return render(request, template, context)


class ProductDetailView(View):

    """A view of an individual product in more detail"""

    def get(self, request, product_id, *args, **kwargs):

        product = get_object_or_404(Product, id=product_id)
        images = ProductImage.objects.filter(
            product = product,
        )

        template = 'products/product_detail.html'

        context = {
            'product': product,
            'images' : images
        }

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

        return render(request, 'products/products_view.html')