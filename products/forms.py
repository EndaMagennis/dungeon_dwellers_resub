from django.forms import ModelForm
from django.forms import forms
from django.forms import ClearableFileInput
from cloudinary.models import CloudinaryField


from .models import Product, Category, Tag, ProductImage

from django import forms

# Override ClearableFileInput to allow Multiple uploads
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# Create a multipleFileField to allow multiple image uploads
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ProductForm(ModelForm):
    """Form for uploading new product"""
    images = MultipleFileField()
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', 'created_at', 'updated_at', 'is_active', 'sku', 'rating')
        widgets = {
            'images': MultipleFileField()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].queryset = Category.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()

class ProductImageForm(ModelForm):
    """Form for uploading product images"""

    class Meta:
        model = ProductImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        