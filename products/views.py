from django.views import View
from django.shortcuts import render, redirect, reverse, get_object_or_404
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

        product_form = ProductForm(instance=ProductImage)
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
            return render(request, 'products/products_add.html', context)
        return redirect('products')
