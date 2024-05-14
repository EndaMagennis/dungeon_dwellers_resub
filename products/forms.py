from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Product, Category, Tag, ProductImage


class ProductForm(ModelForm):
    """Form for uploading new product"""
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug', 'created_at', 'updated_at', 'is_active', 'sku', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].queryset = Category.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()
        # crispy-forms helper
        self.helper = FormHelper()
        self.helper.form_id = 'product-form'
        self.helper.method = 'post'
        self.helper.action = 'add_product'

        self.helper.add_input(Submit('submit', 'Submit'))


class ProductImageForm(ModelForm):
    """Form for uploading product images"""
    class Meta:
        model = ProductImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        