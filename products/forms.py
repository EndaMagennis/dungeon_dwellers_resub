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
    images = MultipleFileField(
        required=False, 
        help_text= 'Hold "Ctrl" while clicking to select mulitple images'
    )
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', 'created_at', 'updated_at', 'is_active', 'sku', 'rating')
        widgets = {
            'images': MultipleFileField(),
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 15}),
            'is_featured': forms.CheckboxInput(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    field_order = ['name', 'images', 'category', 'tags', 'description', ...]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        categories = self.fields['category'].queryset = Category.objects.all()
        tags = self.fields['tags'].queryset = Tag.objects.all()
